# AskOtago

AskOtago is a tounge-in-cheek response to the University of Otago censoring
issue 12 of Critic - The Menstruation Issue. Let the content flow; post to
your heart's content.

Text posts, comments, votes, and that's it.

This also doubles as a research project for SURV319 Geospatial Analysis and
Programming; By adding a location to a post, we can answer some important
questions. Which street has better banter, Castle or Hyde? Is AskOtago most
active during a long lecture? Is everything on this site fabricated in the
Critic office?

![](docs/homepage.png)



# Project architecture

AskOtago is a Django project contained inside a Docker container, to be run
with PostgresQL with GIS extensions. Currently the development version is
hosted on Heroku, at https://askotagodev.herokuapp.com

# Features

As of writing, only text posts and comment responses are functional. Votes
are next to be added, and then location support (collecting, and displaying
nearby landmarks). After that it'd be refinements, for a deadline of 27 Aug
2018 (so it can be tested before Critic returns for the semester break).

To flesh out the project (time pending), it should be converted to a REST API
(django-rest-framework) with a React (etc) frontend, with live updating (AJAX)
, spam filtering (see Azure Cognitive Library), and votes should be extended
to reacting with any emoji, and activity should be displayed on a map of
locations and landmarks (so raw point data isn't available to the end user).

To continue the project after the paper ends, picture uploading, a group
mechanism, and a native mobile app can be added, and the project can be
rebranded as the Otago Computer Science Society Feed.


# Build Instructions

* Install `docker-ce` and `docker-compose`
* Clone this repository
* Run `docker-compose build`
* Run `docker-compose up` - this will fail on the first run as the web
    container starts while Postgres is still initialising
* Run `docker-compose up -d` from repo directory
* Visit `127.0.0.1:8080/`
* Run `docker-compose down` to stop containers

If you need to exec in to the container, to run a command such as
`python3 manage.py createsuperuser`, gather the container ID with `docker ps`
(first few characters will do), and run `docker exec -it <container ID> sh`.

# IDE

* Set up Windows Subsystem for Linux
* Clone repository on to Windows drive so IDE can access files.
* (WSL) Create python virtualenv, and install pip requirements
* (WSL) Install libgdal-dev
* Connect PyCharm using virtualenv python as remote interpreter
* Set dockerfile as PyCharm's build configuration
