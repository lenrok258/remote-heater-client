#!/usr/bin/env bash

LOG_FILE=./logs/`date +%Y-%m-%d_%H:%M.log`

cd $(dirname $0)

source $HOME/.profile

./pull_restart.sh | tee $LOG_FILE 2>&1