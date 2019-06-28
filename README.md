# Django AIO

<p align="center">
	<img src="https://github.com/101t/django-aio/blob/master/main/static/assets/img/django-aio.png" alt="Django AIO">
</p>

Django AIO (All-In-One) to get project ready to develop with my flavor configurations.

Django AIO configured and installed to be compatible with:

1. Django
2. Celery
3. Channels
4. Postgres
5. Redis

Also has some features customization:

1. Custom User
2. Custom sending Mail
3. Sending Notification via channels
4. loggin everything in the system
5. custom sample data loader `python manage.py load_new` and migrations reseter `python manage.py reseter`
6. custom utils functions
7. easy to deployments
8. easy to translate
9. seperating `config/` for configurations and `main/` for all `apps`, `static`, `templates`


## Getting Started

In your terminal for **Unix** (Linux/Mac)

```sh
git clone https://github.com/101t/django-aio

cd django-aio/

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.pip

./load_data.sh --reset
```

In Command Prompt for **Windows**

```sh
git clone https://github.com/101t/django-aio

cd django-aio/

python -m pip install virtualenv

python -m virtualenv env

env/Scripts/activate

pip install -r requirements.pip

./load_data.sh --reset
```

## Conclusion

The `django-aio` repository is a great experience with developing a bigger application in a team of people. We enjoyed the time spent on the project, the quick-starting the implementation with all the nice features we thought of. Our implementation meets our predefined goals and is ready to be deployed quickly with as base templates.