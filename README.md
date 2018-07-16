# Feed

Lightweight, geographically based social network.

## Project Information

This started out as a plain Django application on Heroku, but issues with GDAL
resulted in a switch to Docker. Fingers crossed it works this time

https://www.fir3net.com/Containers/Docker/how-to-configure-django-gunicorn-inside-a-docker-container.html


## Build and start

``` bash
# build 
docker build -t feed-docker:v1 .

# run
docker run --restart=always -p 8000:8000 -i -t feed-docker:v1
```
