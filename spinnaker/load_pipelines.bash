#!/usr/bin/env bash

curl -X POST -H "Content-Type: application/json" --data-binary @"pipelines/deploy-to-staging.json" http://front50-pipeline.cfapps.io/pipelines

curl -X POST -H "Content-Type: application/json" --data-binary @"pipelines/deploy-to-production.json" http://front50-pipeline.cfapps.io/pipelines