#!/usr/bin/env bash

./load.py $1 pipelines/deploy-to-staging.json front50 /pipelines
./load.py $1 pipelines/deploy-to-production.json front50 /pipelines