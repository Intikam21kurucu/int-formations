#!/bin/bash

# Güncellemeleri kontrol et
apt-get update

# Python3 ve pip yükleyin
apt-get install python -y
apt-get install python3-pip -y

# Gerekli Python kütüphanelerini yükleyin
pip3 install pyfiglet
pip3 install --upgrade google-api-python-client
pip3 install requests

echo "Kütüphaneler başarıyla yüklendi."
