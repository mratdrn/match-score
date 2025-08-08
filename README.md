## English
Match Score API
This project fetches live match scores using an API, stores them in Redis, and serves them via a Flask API.

Installation
Install required packages:

pip install -r requirements.txt
Place your .env file in the root directory of the project and insert your API key.

Note: Make sure your Redis server is running.

Running
Use Python directly:

python app.py         # To fetch data and store it in Redis  
python flaskApı.py    # To start the Flask API

API
GET /scores — Returns live scores and calculated data such as over 2.5 goals, both teams to score, and match winner in JSON format.

## Türkçe
Match Score API
Bu proje canlı maç skorlarını Redis üzerinden çekip, Flask API ile servis eden bir uygulamadır.

Kurulum
Gerekli paketleri yükleyin:

pip install -r requirements.txt
.env dosyanızı projenizin kök dizinine koyun ve API anahtarınızı girin.

Not: Redis server’ınızın çalıştığından emin olun.

Çalıştırma
Direkt Python ile

python app.py  # Verileri çekip Redis’e kaydetmek için
python flaskApı.py  # Flask API’yi başlatmak için

API
GET /scores — Canlı skorları ve hesaplanan 2.5 üst, karşılıklı gol, kazanan bilgilerini JSON olarak döner.
