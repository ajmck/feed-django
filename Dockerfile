# Base Image - Alpine Linux
FROM alpine:3.8

MAINTAINER Maintainer Alex McKirdy

RUN apk add \
	python-dev \
	python \
	py-pip \
	git 

# Geospatial libraries in edge repo
# https://github.com/appropriate/docker-postgis/blob/master/Dockerfile.alpine.template
# RUN apk add --no-cache --virtual .build-deps-testing \
# 	--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
# 	gdal-dev \
# 	geos-dev

ENV PROJECT=feed
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

# Create application subdirectories
WORKDIR $CONTAINER_HOME
RUN mkdir logs

# Copy application source code to $CONTAINER_PROJECT
COPY . $CONTAINER_PROJECT

# install python dependencies
RUN pip install pipenv
RUN pipenv install

# Copy and set entrypoint
WORKDIR $CONTAINER_PROJECT
COPY ./entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
