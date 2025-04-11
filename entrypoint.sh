#!/bin/bash



export $(grep -v '^#' .env | xargs)

sleep 2

python manage.py makemigrations
python manage.py migrate
python manage.py create_default_admin

python manage.py runserver 0.0.0.0:8000



exec "$@"