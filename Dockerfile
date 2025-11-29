# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base

# Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

# Application settings
ENV APP_DIR=/app \
    APP_USER=app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    libpq5 \
    libjemalloc2 \
    && rm -rf /var/lib/apt/lists/*

# Use jemalloc for better memory management
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2

# Install uv package manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create non-root user
RUN useradd -m -d ${APP_DIR} -U -r -s /bin/bash ${APP_USER}

WORKDIR ${APP_DIR}

# Copy dependency files first for better caching
COPY --chown=${APP_USER}:${APP_USER} pyproject.toml ./

# Install dependencies using uv (creates virtual environment automatically)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

# Copy application code
COPY --chown=${APP_USER}:${APP_USER} . .

# Create required directories
RUN mkdir -p media public/static logs \
    && chmod +x entrypoint.sh entrypoint-celery.sh \
    && chown -R ${APP_USER}:${APP_USER} ${APP_DIR}

# Switch to non-root user
USER ${APP_USER}

# Add virtual environment to PATH
ENV PATH="${APP_DIR}/.venv/bin:$PATH" \
    PYTHONPATH="${APP_DIR}"

EXPOSE 8000

ENTRYPOINT ["bash", "entrypoint.sh"]
