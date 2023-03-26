#!/usr/bin/env bash

echo "Run app"
gunicorn --workers=2 'main:create_app()' --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:${APP_PORT}