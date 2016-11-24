Requirements:
- Python 2.7.x (sudo apt-get install python)
- PIP (sudo apt-get install python-pip)
- virtualenv (pip install virtualenv)

Config:
- cp config/config.json_example config/config.json
- adjust values in config/config.json (local-development has to be set to 'true' if running not on RPI)

How to run:
- locally: ./pull-restart.sh
- cron-job: ./run-cron.sh