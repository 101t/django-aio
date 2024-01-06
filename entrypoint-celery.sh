#!/bin/bash

APP_DIR=${APP_DIR:-/app}
CELERY_LOG_LEVEL=${CELERY_LOG_LEVEL:-warning}
CELERY_LOG_FILE=${CELERY_LOG_FILE:-/app/logs/celery.log}

cd $APP_DIR

source $APP_DIR/env/bin/activate

celery -A config worker -l $CELERY_LOG_LEVEL -f $CELERY_LOG_FILE
