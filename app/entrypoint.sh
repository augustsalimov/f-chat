#!/usr/bin/env bash

echo "Run app"
gunicorn --bind 0.0.0.0:8000 main