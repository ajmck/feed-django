# Base Image - Alpine Linux
FROM alpine:3.8

MAINTAINER Alex McKirdy

ENV PYTHONBUFFERED 1
ENV PROJECT=feed
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# nb - settings module will fall back to .env defined in docker-compose
# defined here for Heroku use
# Also, note that at the time of writing the only package in requirements/debug.txt is wdb debugger
ARG REQUIREMENTS=requirements/production.txt
ENV DJANGO_SETTINGS_MODULE=feed.settings.production

RUN apk add \
	python3-dev \
	py3-pip \
	git \
	py-setuptools \
	py3-psycopg2 \
	netcat-openbsd

# GDAL dependency broke https://github.com/appropriate/docker-postgis/issues/96#issuecomment-439135368
RUN apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main openssl


RUN python3 -m ensurepip

# Geospatial libraries in edge repo
# https://github.com/appropriate/docker-postgis/blob/master/Dockerfile.alpine.template
RUN apk add --no-cache --virtual .build-deps-testing \
	--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
	gdal-dev \
	geos-dev \
	proj4-dev \
	gdal \
	geos \
	proj4 \
	py-gdal


# pip https://docs.docker.com/compose/django/
RUN mkdir /code
WORKDIR /code
ADD requirements /code/requirements
RUN pip3 install --upgrade pip
# ADD . /code/
RUN pip3 install -r $REQUIREMENTS


# Create application subdirectories
WORKDIR $CONTAINER_HOME
RUN mkdir logs

# Copy application source code to $CONTAINER_PROJECT
# Done after installing dependencies to reduce build time
COPY . $CONTAINER_PROJECT


# Copy and set entrypoint
WORKDIR $CONTAINER_PROJECT
COPY entrypoint.sh /
CMD ["/entrypoint.sh"]
