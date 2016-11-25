#!/usr/bin/env bash

LOG_FILE=./logs/setup_`date +%Y-%m-%d_%H:%M.log`

function log {
    echo $1 | tee -a ${LOG_FILE}
}

ANY_CHANGES=$(git fetch --dry-run 2>&1)

if [ ! -z "${ANY_CHANGES}" ]; then
    log 'New changes found in git. About to pull them and restart Remote Heater client';
    kill $(ps aux | grep -v "grep" | grep "remote-heater-client" | awk '{print $2}') | tee -a ${LOG_FILE}
    sleep 5
    git reset --hard | tee -a ${LOG_FILE}
    git pull --force | tee -a ${LOG_FILE}
fi;

IS_RUNNING=$(ps aux | grep -v grep | grep "remote-heater-client.py")

if [ -z "${IS_RUNNING}" ]; then
    log 'Remote Heater client does not seem to work. About to start it.';
    ./install.sh | tee -a ${LOG_FILE}
    ./run-remote-heater-client.sh
fi