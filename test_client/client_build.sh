#!/bin/bash

docker rmi client-image
docker build -t client-image .