#!/usr/bin/env bash

LOG_FILE=./logs/`date +%Y-%m-%d_%H:%M.log`

function log {
    echo $1 | tee -a $LOG_FILE
}

ANY_CHANGES=$(git fetch --dry-run 2>&1)

if [ ! -z "${ANY_CHANGES}" ]; then
    log 'New changes found on git. About to pull them and restart Remote Heater client';
    killall runme.py | tee -a $LOG_FILE
    git reset --hard | tee -a $LOG_FILE
    git pull --force | tee -a $LOG_FILE
fi;

IS_RUNNING=$(ps cax | grep runme.py)

if [ -z "${IS_RUNNING}" ]; then
    log 'Remote Heater client does not seem to work. About to start it.';
    ./install.sh | tee -a $LOG_FILE
    ./.env/bin/python -u ./runme.py | tee -a $LOG_FILE
fi;