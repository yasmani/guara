#!/bin/bash

echo "=== DIAGNÓSTICO DE BASE DE DATOS ==="

# 1. Verificar si el archivo existe y su tamaño
if [ -f db.sqlite3 ]; then
    SIZE=$(ls -lh db.sqlite3 | awk '{print $5}')
    echo "✅ db.sqlite3 encontrado - Tamaño: $SIZE"
    
    # 2. Mostrar cuántas tablas tiene
    TABLE_COUNT=$(sqlite3 db.sqlite3 "SELECT COUNT(*) FROM sqlite_master WHERE type='table';" 2>/dev/null)
    echo "📊 Número de tablas en la base de datos: $TABLE_COUNT"
    
    # 3. Verificar que la tabla 'marcas' existe y tiene datos
    MARCA_COUNT=$(sqlite3 db.sqlite3 "SELECT COUNT(*) FROM marcas;" 2>/dev/null || echo "0")
    echo "📊 Registros en tabla 'marcas': $MARCA_COUNT"
    
    # 4. Mostrar primeras 5 marcas como ejemplo
    echo "📋 Ejemplo de marcas:"
    sqlite3 db.sqlite3 "SELECT * FROM marcas LIMIT 3;" 2>/dev/null || echo "No se pudo leer"
    
else
    echo "❌ ERROR: db.sqlite3 NO EXISTE en /app"
    echo "Contenido del directorio /app:"
    ls -la /app
    exit 1
fi

echo ""
echo "=== EJECUTANDO MIGRACIONES ==="
python manage.py migrate --noinput

echo ""
echo "=== INICIANDO GUNICORN ==="
gunicorn guara.wsgi:application --bind 0.0.0.0:10000