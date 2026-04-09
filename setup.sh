#!/bin/bash

echo "=== DIAGNÓSTICO DE BASE DE DATOS ==="
echo "Directorio actual: $(pwd)"

# Verificar existencia de db.sqlite3
if [ -f db.sqlite3 ]; then
    SIZE=$(ls -lh db.sqlite3 | awk '{print $5}')
    echo "✅ db.sqlite3 encontrado - Tamaño: $SIZE"
    
    # Verificar columnas de home_usuarios
    echo ""
    echo "📋 Columnas de la tabla 'home_usuarios':"
    sqlite3 db.sqlite3 "PRAGMA table_info(home_usuarios);"
    
    echo ""
    echo "📋 Datos de la tabla 'home_usuarios':"
    sqlite3 db.sqlite3 "SELECT * FROM home_usuarios LIMIT 5;"
else
    echo "❌ db.sqlite3 NO encontrado"
    exit 1
fi

echo ""
echo "=== EJECUTANDO MIGRACIONES ==="
python manage.py migrate --noinput

echo ""
echo "=== INICIANDO GUNICORN ==="
gunicorn guara.wsgi:application --bind 0.0.0.0:10000