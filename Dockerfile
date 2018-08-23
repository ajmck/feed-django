# Base Image - Alpine Linux
FROM alpine:3.8

MAINTAINER Maintainer Alex McKirdy

ENV PYTHONBUFFERED 1

ARG REQUIREMENTS=requirements/production.txt
ENV DJANGO_SETTINGS_MODULE=feed.settings.production

RUN apk add \
	python3-dev \
	py3-pip \
	git \
	py-setuptools \
	py3-psycopg2 \
	netcat-openbsd

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

ENV PROJECT=feed
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# Create application subdirectories
WORKDIR $CONTAINER_HOME
RUN mkdir logs

# Copy application source code to $CONTAINER_PROJECT
COPY web $CONTAINER_PROJECT

# pip https://docs.docker.com/compose/django/
RUN mkdir /code
WORKDIR /code
ADD web/requirements /code/requirements
RUN pip3 install --upgrade pip
ADD web /code/
RUN pip3 install -r $REQUIREMENTS


# Copy and set entrypoint
WORKDIR $CONTAINER_PROJECT
COPY web/entrypoint.sh /
CMD ["/entrypoint.sh"]
