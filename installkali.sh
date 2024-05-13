#!/bin/bash

# Güncellemeleri kontrol et
sudo apt-get update

# Python3 ve pip yükleyin
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y

# Gerekli Python kütüphanelerini yükleyin
sudo pip3 install pyfiglet
sudo pip3 install --upgrade google-api-python-client
sudo pip3 install requests

echo "Kütüphaneler başarıyla yüklendi."
