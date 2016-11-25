#!/usr/bin/env bash

LOG_FILE=./logs/setup_`date +%Y-%m-%d_%H:%M.log`

function log {
    echo $1 | tee -a ${LOG_FILE}
}

ANY_CHANGES=$(git fetch --dry-run 2>&1)

if [ ! -z "${ANY_CHANGES}" ]; then
    log 'New changes found in git. About to pull them and restart Remote Heater client';
    kill $(ps aux | grep -v grep | grep "./run-remote-heater-client.sh" | awk '{print $2}') | tee -a ${LOG_FILE}
    sleep 5
    git reset --hard | tee -a ${LOG_FILE}
    git pull --force | tee -a ${LOG_FILE}
else
    log 'No new changes found in git'
fi;

IS_RUNNING=$(ps aux | grep -v grep | grep "./run-remote-heater-client.sh")

if [ -z "${IS_RUNNING}" ]; then
    log 'Remote Heater client does not seem to work. About to start it.';
    ./install.sh | tee -a ${LOG_FILE}p
    ./run-remote-heater-client.sh
else
    log 'Remote Heater already started - nothing to do.'
fi