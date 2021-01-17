#!/bin/bash

set -e

image_name="aioredis-models:latest"
docker build -t $image_name .
docker run -it --rm -v $PWD/test-reports:/home/test-reports $image_name $*