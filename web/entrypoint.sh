#! /bin/bash

set -e

cd /src

# python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py migrate auth
python3 manage.py migrate app
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py runserver 0.0.0.0:8000