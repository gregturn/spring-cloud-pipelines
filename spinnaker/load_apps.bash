#!/usr/bin/env bash

curl -X POST -H "Content-Type: application/json" --data-binary @"applications/demo.json" http://front50-pipeline.cfapps.io/v2/applications