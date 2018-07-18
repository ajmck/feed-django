#!/bin/sh


# Prepare log files and start outputting logs to stdout
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log
tail -n 0 -f ./logs/gunicorn*.log &

export DJANGO_SETTINGS_MODULE=feed.settings



# pip3 install --upgrade pip
# pip3 install -r requirements.txt
python3 manage.py migrate 
python3 manage.py collectstatic --noinput

exec gunicorn feed.wsgi \
    --name feed \
    --bind 0.0.0.0:8080 \
    --workers 5 \
"$@"


# extra gunicorn args removed for debugging

#     --log-level=info \
#     --log-file=./logs/gunicorn.log \
#     --access-logfile=./logs/gunicorn-access.log \
