#!/bin/bash

set -e

python3 ./colorbrains_api/scripts/populate_database.py
uvicorn main:app --host 0.0.0.0 --port 80
