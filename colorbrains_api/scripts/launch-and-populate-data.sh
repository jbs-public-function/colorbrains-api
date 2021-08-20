#!/bin/bash
python3 /app/scripts/populate_database.py
uvicorn main:app --host 0.0.0.0 --port 80