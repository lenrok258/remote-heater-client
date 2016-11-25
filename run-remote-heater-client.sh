#!/usr/bin/env bash

LOG_FILE=./logs/run_`date +%Y-%m-%d_%H:%M.log`

./.env/bin/python -u ./runme.py | tee -a ${LOG_FILE}

