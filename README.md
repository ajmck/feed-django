# Feed

Lightweight, geographically based social network.

## Project Information

This started out as a plain Django application on Heroku, but issues with GDAL
resulted in a switch to Docker. Fingers crossed it works this time

https://www.fir3net.com/Containers/Docker/how-to-configure-django-gunicorn-inside-a-docker-container.html

https://alexurquhart.com/post/set-up-postgis-with-docker/

# Build Instructions

* Install `docker-ce` and `docker-compose`
* Clone this repository
* Run `docker-compose build`
* Run `docker-compose up` - this will fail on the first run as the web container starts while Postgres is still initialising 
* Run `docker-compose up -d` from repo directory
* Visit `127.0.0.1:8080/core`
* Run `docker-compose down` to stop containers

# IDE
* Set up Windows Subsystem for Linux
* Create python virtualenv, and install pip requirements
* Install libgdal-dev
* Connect PyCharm using virtualenv python as remote interpreter
* Set dockerfile as PyCharm's build configuration
