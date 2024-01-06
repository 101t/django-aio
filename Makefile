# Variables definitions
# -----------------------------------------------------------------------------

TIMEOUT ?= 60

# Determine the OS platform (Windows or Linux)
ifeq ($(OS),Windows_NT)
	SHELL := cmd.exe
	RM := del /Q
	EXE := .exe
else
	SHELL := /bin/bash
	RM := rm -rf
	EXE :=
endif


# Target section and Global definitions
# -----------------------------------------------------------------------------
.PHONY: all clean test install run deploy down

all: clean test install run deploy down

test:
	python -m pytest tests -vv --show-capture=all

install: generate_dot_env
	pip install --upgrade pip wheel
	pip install -r requirements.txt

run:
	PYTHONPATH=. python manage.py runserver 0.0.0.0:8000

run_uvicorn:
	PYTHONPATH=. uvicorn config.asgi:application --reload --host 0.0.0.0 --port 8000

run_celery:
	PYTHONPATH=. celery -A config worker --max-tasks-per-child 1 -l info

run_channels:
	PYTHONPATH=. daphne config.asgi:application -b 0.0.0.0 -p 9000

run_docker: generate_dot_env
	docker-compose build
	docker-compose up

generate_dot_env:
	@if [ ! -e .env ]; then \
		cp sample.env .env; \
	fi

make_migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

clean:
	$(RM) *.pyc
	$(RM) -r __pycache__
	$(RM) Thumbs.db
	$(RM) *~
	$(RM) .cache
	$(RM) build
	$(RM) dist
	$(RM) *.egg-info
	$(RM) htmlcov
	$(RM) .tox/
	$(RM) -r docs/_build
	$(RM) .env

