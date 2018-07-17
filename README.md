# Feed

Lightweight, geographically based social network.

## Project Information

This started out as a plain Django application on Heroku, but issues with GDAL
resulted in a switch to Docker. Fingers crossed it works this time

https://www.fir3net.com/Containers/Docker/how-to-configure-django-gunicorn-inside-a-docker-container.html


## Build and start

Set up a PostGIS database container (which ought to be unnecessary when (if?)
hosting on Heroku).

https://alexurquhart.com/post/set-up-postgis-with-docker/


```
docker volume create pg_data
docker run --name=postgis -d -e POSTGRES_USER=feed_user -e POSTGRES_PASS=feed_password -e POSTGRES_DBNAME=feed_db -e ALLOW_IP_RANGE=0.0.0.0/0 -p 5432:5432 -v pg_data:/var/lib/postgresql --restart=always mdillon/postgis
```

``` bash
# build 
docker build -t feed-docker:v1 .

# run
docker run --restart=always -p 8000:8000 -i -t feed-docker:v1
```
