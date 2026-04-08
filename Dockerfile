FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY . .

# VERIFICAR que db.sqlite3 se copió correctamente
RUN ls -la db.sqlite3 && \
    echo "✅ db.sqlite3 copiado - tamaño: $(du -h db.sqlite3 | cut -f1)"
    
# Dar permisos de ejecución al script
RUN chmod +x setup.sh

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=guara.settings

# Puerto
EXPOSE 10000

# Ejecutar el script de inicio
CMD ["./setup.sh"]