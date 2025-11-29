#!/bin/bash
set -e

# Configuration with defaults
PORT=${PORT:-8000}
WORKERS=${WORKERS:-4}
LOG_LEVEL=${LOG_LEVEL:-info}
WORKER_CLASS=${WORKER_CLASS:-uvicorn.workers.UvicornWorker}

echo "[DjangoAIO] Running migrations..."
python manage.py migrate --noinput

echo "[DjangoAIO] Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "[DjangoAIO] Starting server on port $PORT with $WORKERS workers..."
exec gunicorn config.asgi:application \
    --bind 0.0.0.0:"$PORT" \
    --workers "$WORKERS" \
    --worker-class "$WORKER_CLASS" \
    --timeout 120 \
    --graceful-timeout 30 \
    --keep-alive 5 \
    --log-level "$LOG_LEVEL" \
    --access-logfile - \
    --error-logfile -

