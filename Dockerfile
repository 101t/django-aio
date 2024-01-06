FROM python:3.11-slim

# disable debian interactive
ENV DEBIAN_FRONTEND noninteractive
ENV PIP_NO_CACHE_DIR 1
ENV PYTHONUNBUFFERED 1

ENV APP_DIR /app
ENV APP_USER app

RUN apt-get update && apt-get -y upgrade

RUN apt-get install --no-install-recommends -y \
    python3-dev python3-wheel python3-setuptools virtualenv \
    build-essential nano gcc curl \
    libpq-dev libpq5 telnet \
    libjemalloc2

RUN apt-get clean autoclean && apt-get autoremove -y && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

ENV LD_PRELOAD /usr/lib/x86_64-linux-gnu/libjemalloc.so.2

RUN useradd -m -d ${APP_DIR} -U -r -s /bin/bash ${APP_USER}

USER ${APP_USER}

WORKDIR ${APP_DIR}

RUN python -m venv /app/env

ENV PATH="$APP_DIR/env/bin:$PATH"

RUN mkdir media static logs

COPY requirements.txt .

RUN pip install -U pip wheel

RUN pip install -r requirements.txt

COPY --chown=$APP_USER . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN chmod +x entrypoint.sh
RUN chmod +x entrypoint-celery.sh

RUN chown -R app: $APP_DIR

ENTRYPOINT ["bash", "entrypoint.sh"]
