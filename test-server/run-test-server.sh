#!/bin/bash

while [ 1 ]; do
    cat ./test-response.txt | nc -l 8001
done;