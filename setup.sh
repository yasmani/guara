#!/bin/bash

# Instalar Python 3.11
apt-get update
apt-get install -y python3.11 python3.11-dev python3.11-distutils

# Instalar pip para Python 3.11
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.11

# Instalar dependencias directamente con Python 3.11
python3.11 -m pip install --upgrade pip
python3.11 -m pip install -r requirements.txt