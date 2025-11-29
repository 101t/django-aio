# DjangoAIO Makefile
# Using uv as package manager
# -----------------------------------------------------------------------------

.DEFAULT_GOAL := help
.PHONY: help install dev test lint format run run-uvicorn run-celery docker-up docker-down clean migrate makemigrations

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Setup & Installation
install: .env  ## Install production dependencies
	uv sync --frozen --no-dev

dev: .env  ## Install all dependencies including dev tools
	uv sync

.env:
	cp sample.env .env

# Development Commands
run: .env  ## Run Django development server
	uv run python manage.py runserver 0.0.0.0:8000

run-uvicorn: .env  ## Run with uvicorn (ASGI)
	uv run uvicorn config.asgi:application --reload --host 0.0.0.0 --port 8000

run-celery: .env  ## Run Celery worker
	uv run celery -A config worker -l info

run-beat: .env  ## Run Celery beat scheduler
	uv run celery -A config beat -l info

# Database Commands
migrate: .env  ## Run database migrations
	uv run python manage.py migrate

makemigrations: .env  ## Create new migrations
	uv run python manage.py makemigrations

createsuperuser: .env  ## Create admin user
	uv run python manage.py createsuperuser

shell: .env  ## Open Django shell
	uv run python manage.py shell

# Testing & Quality
test: .env  ## Run tests
	uv run pytest -v

test-cov: .env  ## Run tests with coverage
	uv run pytest --cov=main --cov-report=html

lint:  ## Run linter
	uv run ruff check .

format:  ## Format code
	uv run ruff format .

# Docker Commands
docker-build:  ## Build Docker image
	docker compose build

docker-up: .env  ## Start all services
	docker compose up -d

docker-down:  ## Stop all services
	docker compose down

docker-logs:  ## View logs
	docker compose logs -f

# Cleanup
clean:  ## Clean up generated files
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	find . -type d -name '.ruff_cache' -exec rm -rf {} +
	rm -rf htmlcov .coverage dist build *.egg-info

