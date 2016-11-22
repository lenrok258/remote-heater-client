#!/usr/bin/env bash

ANY_CHANGES=$(git fetch --dry-run 2>&1)
RUNME_RUNNING=$(ps cax | grep runme.py)

if [ ! -z "${ANY_CHANGES}" ]; then
    echo 'New changes found on git. About to pull them and restart Remote Heater client';
    killall runme.py
    git pull --force
fi;

if [ -z "${RUNME_RUNNING}" ]; then
    echo 'Remote Heater client does not seem to work. About to start it.';
    ./install.sh
    ./runme.py
fi;