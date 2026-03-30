FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primero
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY . .

# Ejecutar migraciones y recolectar archivos estáticos
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Variables de entorno
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=guara.settings

# Puerto
EXPOSE 10000

# Comando
CMD ["gunicorn", "guara.wsgi:application", "--bind", "0.0.0.0:10000"]