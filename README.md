<h1 align="center">Django AIO</h1>
<p align="center">
	<img src="main/static/assets/img/django-aio.png" alt="Django AIO">
</p>
<p>
	<a href="https://travis-ci.org/101t/django-aio"><img src="https://travis-ci.org/101t/django-aio.svg?branch=master" alt="travis-ci"></a>
	<a href='https://coveralls.io/github/101t/django-aio'><img src='https://coveralls.io/repos/github/101t/django-aio/badge.svg' alt='Coverage Status' /></a>
</p>

## Features I thought About

Django AIO (All-In-One) to get project ready to develop with my flavor configurations.

All in one pre-configured and prepared as django project, your project will be ready to use:

1. Django
2. Celery
3. Channels
4. Postgres
5. Redis
6. DRF (Django REST Framework, Swagger, JWT)

Also has some features' customization:

1. Custom User
2. Custom sending Mail
3. Sending Notification via channels
4. login everything in the system
5. custom sample data loader `python manage.py load_new` and migrations reseter `python manage.py reseter`
6. custom utils functions
7. easy to deployments
8. easy to translate
9. separating `config/` for configurations and `main/` for all `apps`, `static`, `templates`
10. Pre-configured API using JWT authentication and swagger-ui


## Getting Started

In your terminal for **Unix** (Linux/Mac)

```shell
pip install virtualenv

git clone https://github.com/101t/django-aio --depth 1

cd django-aio/

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

cp sample.env .env

python manage.py migrate

python manage.py load_new

python manage.py runserver
```

In Command Prompt for **Windows**

```shell
python -m pip install virtualenv

git clone https://github.com/101t/django-aio --depth 1

cd django-aio/

virtualenv env

env/Scripts/activate

pip install -r requirements.txt

copy sample.env .env

python manage.py migrate

python manage.py load_new

python manage.py runserver
```

Or using as new project templates

```shell
django-admin.py startproject --template=https://github.com/101t/django-aio/archive/latest.zip --extension=py,gitignore YOUR_PROJECT_NAME
```

> Note: the `admin` user automatically added to project as default administrator user, the credentials authentication is **Username: `admin`, Password: `secret`**.

## Development

### Prepare Translations

Adding translation made easy by this commands

```shell
cd django-aio/main/

django-admin makemessages -l en

django-admin compilemessages
```
> Note: make sure you have `gettext` installed in your `Unix` Environment

```shell
# using gettext in ubuntu or macOS
msgunfmt [django.mo] > [django.po]
```

### Run Celery

To run your celery in development
```shell
make run_celery
```

### Run Django
To run django in development as `HTTP` 
```shell
make run
```

## Conclusion

The `django-aio` [Django All-in-One] repository is the result of years of development to starts from the middle of project-life. 
The repository represent predefined goals and base templates for django frameworks and its beautiful 3rd-party packages.