# Django AIO

<p align="center">
  <img src="main/static/assets/img/django-aio.png" alt="Django AIO">
</p>

**Django AIO (All-In-One)** - A modern, production-ready Django starter template with batteries included.

## Features

- **Django 5.2+** - Latest Django with async support
- **REST API** - Django REST Framework with JWT authentication and OpenAPI docs (drf-spectacular)
- **WebSockets** - Django Channels for real-time features
- **Task Queue** - Celery with Redis backend
- **Database** - PostgreSQL support with connection pooling
- **Modern Tooling** - Uses [uv](https://github.com/astral-sh/uv) for fast dependency management
- **Docker Ready** - Optimized Dockerfile and docker-compose for production
- **Admin UI** - Django Jet Reboot for beautiful admin interface

### Project Structure

```
django-aio/
├── config/          # Django configuration (settings, urls, asgi, celery)
├── main/            # All Django apps
│   ├── api/         # REST API endpoints
│   ├── core/        # Core utilities and shared code
│   ├── notify/      # WebSocket notifications
│   ├── users/       # Custom user model
│   └── web/         # Web views and templates
├── deployment/      # Nginx, systemd configs
├── pyproject.toml   # Dependencies (uv/pip)
└── Makefile         # Common commands
```


## Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation with uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/101t/django-aio --depth 1
cd django-aio

# Install dependencies and create .env
make dev

# Run migrations and start the server
make migrate
make run
```

### Installation with pip

```bash
# Clone and setup
git clone https://github.com/101t/django-aio --depth 1
cd django-aio

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -e .

# Setup environment
cp sample.env .env

# Run the application
python manage.py migrate
python manage.py runserver
```

### Using Docker

```bash
# Start all services (web, celery, postgres, redis)
make docker-up

# View logs
make docker-logs

# Stop services
make docker-down
```

> **Note:** Default admin credentials: **Username: `admin`, Password: `secret`**

## Development

### Available Commands

```bash
make help              # Show all available commands
make run               # Run Django development server
make run-uvicorn       # Run with uvicorn (ASGI)
make run-celery        # Run Celery worker
make migrate           # Run database migrations
make makemigrations    # Create new migrations
make test              # Run tests
make lint              # Run linter (ruff)
make format            # Format code
```

### API Documentation

Once the server is running, access the API docs at:
- **Swagger UI:** http://localhost:8000/api/docs/
- **ReDoc:** http://localhost:8000/api/redoc/

### Translations

```bash
cd main/
django-admin makemessages -l en
django-admin compilemessages
```

## Production Deployment

### Docker (Recommended)

The included `Dockerfile` uses multi-stage builds with uv for fast, small images:

```bash
docker compose build
docker compose up -d
```

### Manual Deployment

See `deployment/` for:
- Nginx configuration
- Systemd service files
- Gunicorn setup

## Environment Variables

See `sample.env` for all available configuration options.

Key settings:
- `SECRET_KEY` - Django secret key (generate a new one for production)
- `DEBUG` - Set to `False` in production
- `PRODB_URL` - PostgreSQL connection string
- `REDIS_HOST` - Redis hostname
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts

## License

MIT License