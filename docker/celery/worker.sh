#!/usr/bin/env sh

# Use named queue if passed or default one:
QUEUE_NAME=${1:-'default'}
echo "[starting worker for queue: ${QUEUE_NAME}]"

# Runs celery worker with events sourcing to monitoring:
celery --app=server.celery_app:app worker -E -B -Q "$QUEUE_NAME"
