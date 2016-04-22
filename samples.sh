#!/bin/bash

# Acessando o postgres
docker-compose run -u postgres db cat /docker-entrypoint.sh

# Executado migrate
docker-compose run web /usr/local/bin/python manage.py makemigrations
docker-compose run web /usr/local/bin/python manage.py migrate