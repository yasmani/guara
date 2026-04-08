#!/bin/bash

echo "=== DIAGNÓSTICO DE BASE DE DATOS ==="

# Verificar tabla home_usuarios
echo "🔍 Verificando tabla home_usuarios..."
sqlite3 db.sqlite3 <<EOF
.mode column
.headers on
SELECT id, nombre, username, cargo, estado FROM home_usuarios LIMIT 10;
EOF

echo ""
echo "=== CONTINUANDO CON EL INICIO NORMAL ==="

# Resto de tu setup.sh original...
python manage.py migrate --noinput
python manage.py makemigrations --noinput
python manage.py collectstatic --noinput --clear
gunicorn guara.wsgi:application --bind 0.0.0.0:10000