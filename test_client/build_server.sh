#!/bin/bash

docker rmi server-image
docker build -t server-image -f ../src/Dockerfile