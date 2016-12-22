#!/bin/bash

cd $(dirname $0)

find ./logs ! -name .gitkeep -type f -mtime +7 -delete