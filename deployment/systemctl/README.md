# DjangoAIO Systemd Deployment

This guide explains how to deploy DjangoAIO using systemd on a Linux server.

## Prerequisites

- Ubuntu 22.04+ or similar Linux distro
- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- Nginx
- uv (Python package manager)

## Initial Setup

### 1. Create System User

```bash
sudo useradd -r -m -d /opt/djangoaio -s /bin/bash djangoaio
```

### 2. Clone and Install

```bash
sudo -u djangoaio bash
cd /opt/djangoaio

# Clone repository
git clone https://github.com/101t/django-aio .

# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync --frozen --no-dev

# Create directories
mkdir -p logs public/static public/media

# Setup environment
cp sample.env .env
# Edit .env with production values
nano .env
```

### 3. Configure Database

Edit `.env` and set:
```
PRODB_URL=postgres://djangoaio:password@localhost:5432/djangoaio
DJANGO_SETTINGS_MODULE=config.settings.pro
DEBUG=False
SECRET_KEY=your-secure-secret-key
ALLOWED_HOSTS=your-domain.com
```

### 4. Run Migrations

```bash
source .venv/bin/activate
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

## Install Service Files

```bash
# Copy service files
sudo cp deployment/systemctl/*.service /etc/systemd/system/

# Reload systemd
sudo systemctl daemon-reload

# Enable services
sudo systemctl enable djangoaio-gunicorn
sudo systemctl enable djangoaio-celery
sudo systemctl enable djangoaio-celerybeat

# Start services
sudo systemctl start djangoaio-gunicorn
sudo systemctl start djangoaio-celery
sudo systemctl start djangoaio-celerybeat
```

## Service Files

| File | Description |
|------|-------------|
| `djangoaio-gunicorn.service` | Main web application (Gunicorn + Uvicorn workers) |
| `djangoaio-celery.service` | Celery worker for background tasks |
| `djangoaio-celerybeat.service` | Celery beat for scheduled tasks |
| `djangoaio-daphne.service` | Alternative: Daphne ASGI server |

## Useful Commands

```bash
# Check service status
sudo systemctl status djangoaio-gunicorn

# View logs
sudo journalctl -u djangoaio-gunicorn -f

# Restart services
sudo systemctl restart djangoaio-gunicorn

# Stop services
sudo systemctl stop djangoaio-gunicorn
```

## Nginx Configuration

Copy and configure nginx:

```bash
sudo cp deployment/nginx/nginx.conf /etc/nginx/sites-available/djangoaio
sudo ln -s /etc/nginx/sites-available/djangoaio /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## Troubleshooting

### View all logs
```bash
journalctl -u djangoaio-gunicorn -u djangoaio-celery -u djangoaio-celerybeat --since "1 hour ago"
```

### Check service dependencies
```bash
systemctl list-dependencies djangoaio-gunicorn
```

### Restart all services
```bash
sudo systemctl restart djangoaio-gunicorn djangoaio-celery djangoaio-celerybeat