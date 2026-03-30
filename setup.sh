#!/bin/bash
# start.sh

echo "Ejecutando migraciones..."
python manage.py migrate --noinput

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "Iniciando Gunicorn..."
gunicorn guara.wsgi:application --bind 0.0.0.0:10000