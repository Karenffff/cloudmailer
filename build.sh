#!/bin/bash
echo "building the project"
python3 -m pip install -r requirements.txt

echo "make migration.."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "collect static..."
python3 manage.py collectstatic --noinput --clear