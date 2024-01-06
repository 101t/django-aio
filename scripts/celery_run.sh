#!/bin/bash

celery worker -A config -l info --autoscale=10,3