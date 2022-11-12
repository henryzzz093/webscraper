#!/bin/sh


echo "Waiting for MySQL..."

while ! mysqladmin ping -h"$DB_HOST" --silent; 
    do
        sleep 1
    done

echo "MySQL started"

python manage.py flush --no-input
python manage.py migrate
python manage.py createsuperuser --noinput

exec "$@"