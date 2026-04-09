FROM python:3.11-slim

# Cambiar WORKDIR para evitar confusión con la carpeta 'app'
WORKDIR /home/app

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

# Verificar que db.sqlite3 se copió correctamente
RUN ls -la db.sqlite3 && \
    echo "✅ db.sqlite3 copiado - tamaño: $(du -h db.sqlite3 | cut -f1)"

# Verificar la estructura de directorios
RUN echo "=== ESTRUCTURA DE DIRECTORIOS ===" && \
    ls -la && \
    echo "=== CONTENIDO DE CARPETA app ===" && \
    ls -la app/ || echo "app/ no existe"

# Dar permisos de ejecución al script
RUN chmod +x setup.sh

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=guara.settings

# Puerto
EXPOSE 10000

CMD ["./setup.sh"]