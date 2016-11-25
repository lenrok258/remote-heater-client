#!/usr/bin/env bash

LOG_FILE=./logs/run_`date +%Y-%m-%d_%H:%M.log`

./.env/bin/python -u ./remote-heater-client.py | tee -a ${LOG_FILE}

