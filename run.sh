# gunicorn -c gunicorn_config.py setup.wsgi:application
gunicorn --env DJANGO_SETTINGS_MODULE=setup.settings setup.wsgi
