#!/bin/bash

APP_DIR=${APP_DIR:-/app}
PORT=${PORT:-8000}
WORKERS=${WORKERS:-4}
WORKER_CLASS=${WORKER_CLASS:-gevent}

LOG_LEVEL=${LOG_LEVEL:-info}
LOG_FILE=${LOG_FILE:-/app/logs/gunicorn.log}

cd $APP_DIR

source $APP_DIR/env/bin/activate

python -c "from gevent import monkey; monkey.patch_all(thread=False, select=False)"

python manage.py migrate --fake-initial
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn config:wsgi:application \
  --timeout 120 \
  --preload \
  --reload \
  --bind :"$PORT" \
  --workers $WORKERS \
  --worker-class $WORKER_CLASS \
  --log-level "$LOG_LEVEL" \
  --log-file "$LOG_FILE"

