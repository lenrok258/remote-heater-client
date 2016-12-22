#!/bin/bash

cd $(dirname $0)

find ./logs -name 2* -type f -mtime +1 -delete