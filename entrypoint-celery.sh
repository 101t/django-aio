#!/bin/bash
set -e

# Configuration with defaults
CELERY_LOG_LEVEL=${CELERY_LOG_LEVEL:-info}
CELERY_CONCURRENCY=${CELERY_CONCURRENCY:-4}

echo "[DjangoAIO] Starting Celery worker..."
exec celery -A config worker \
    --loglevel="$CELERY_LOG_LEVEL" \
    --concurrency="$CELERY_CONCURRENCY" \
    --optimization=fair
