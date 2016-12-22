#!/bin/bash

cd $(dirname $0)

find ./logs ! -name .gitkeep -type f -mtime +1 -delete