#!/bin/bash
# setup.sh

echo "Instalando Python 3.11..."
apt-get update && apt-get install -y python3.11 python3.11-venv python3.11-dev

echo "Creando entorno virtual con Python 3.11..."
python3.11 -m venv .venv
source .venv/bin/activate

echo "Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt