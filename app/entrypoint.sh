#!/usr/bin/env bash

echo "Run app"
gunicorn main --bind 0.0.0.0:${APP_PORT} -k uvicorn.workers.UvicornWorker