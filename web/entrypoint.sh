#!/bin/sh


# Prepare log files and start outputting logs to stdout
mkdir logs
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log
tail -n 0 -f ./logs/gunicorn*.log &

export DJANGO_SETTINGS_MODULE=feed.settings


# wait for postgres to become available
# https://stackoverflow.com/questions/31746182/docker-compose-wait-for-container-x-before-starting-y/41854997#41854997
# while ! nc -z db 5432; do sleep 3; done
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput

exec gunicorn feed.wsgi \
    --name feed \
    --bind 0.0.0.0:$PORT \
    --workers 5 \
"$@"


# extra gunicorn args removed for debugging

#     --log-level=info \
#     --log-file=./logs/gunicorn.log \
#     --access-logfile=./logs/gunicorn-access.log \
