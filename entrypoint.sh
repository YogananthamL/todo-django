#!/bin/sh

set -e

echo "Database is ready"

echo "Running database migrations"
python3 manage.py migrate

echo "Starting the Django app"
exec python3 manage.py runserver 0.0.0.0:8000
