# ENGLISH

## Match Score API
This project uses an API to fetch live match scores, stores this data in a Redis database, and then serves it through a Flask API. Swagger is also used for API documentation.


## Requirements

- Python 3.7+
- Redis server
- Python packages:
  - flask
  - redis
  - python-dotenv
  - flask-swagger-ui
- API key (see the .env file for details)



## Installation
Install the required Python packages:
`pip install -r requirements.txt`

Create a `.env` file in the project root and add your API key:
 `API_KEY=your_api_key_here`

Make sure the Redis server is running.


## Running
To fetch data and save it to Redis:
  python app.py

To start the Flask API:
  `python flaskApı.py`

After the API is running:
  http://localhost:5000/scores  You can access live scores in JSON format at this address.


## API Usage
GET /scores: Returns live scores and calculated 2.5 over, mutual goal, and winner information in JSON format.

 Example Response;
```
  "live_scores": 
    {
      "25_upper": false,
      "current_winner": 0,
      "home": "Inter Turku",
      "home_score": 0,
      "mutual_goal": false,
      "visitor": "AC Oulu",
      "visitor_score": 0
    }
```


## Docker Support
The project is containerized using Docker.

For the API:

  `docker build -f dockerfile-api -t match-score-api .`
  `docker run -p 5000:5000 match-score-api`
--
For the data fetching service:

  `docker build -f dockerfile-fetcher -t match-score-fetcher .`
  `docker run match-score-fetcher`
--
To start both services together using Docker Compose:

  `docker-compose up`


## Swagger Support
The project uses Swagger for API documentation.
Documentation file: static/swagger.yaml

You can access it in the browser while the Flask application is running:  
 http://localhost:5000/swagger

Swagger UI allows you to visually explore and test API endpoints.


## File Structure
```
match-score/
├── static/
│   └── swagger.yaml      # Swagger API documentation file
├── .dockerignore         # Files ignored by Docker build
├── .env                  # Stores API key and other environment variables
├── .gitignore            # Files ignored by Git
├── app.py                # Manages data fetching and saving to Redis
├── flaskAPI.py           # Flask API server
├── docker-compose.yml    # Docker Compose configuration file
├── Dockerfile-api        # Dockerfile for the API service
├── Dockerfile-fetcher    # Dockerfile for the data fetching service
├── README.md             # General information about the project
├── readscores.py         # Python code that fetches the original score data
└── requirements.txt      # Lists Python dependencies
```

----------

# TÜRKÇE

## Match Score API
Bu proje, canlı maç skorlarını çekmek için bir API kullanır, bu verileri Redis veritabanında saklar ve ardından bir Flask API aracılığıyla sunar. Swagger ile API dokümantasyonu da sağlanmıştır.


## Gereksinimler 

- Python 3.7+
- Redis sunucusu
- Python paketleri:
  - flask
  - redis
  - python-dotenv
  - flask-swagger-ui
- API anahtarı (detaylar için .env dosyasına bakınız)


## Kurulum 
Gerekli Python paketlerini yükleyin:
`pip install -r requirements.txt`

Proje kök dizinine bir .env dosyası oluşturun ve API anahtarınızı ekleyin:
`API_KEY= api_key_buraya_yazın`

Redis sunucusunun çalıştığından emin olun.


## Çalıştırma 
Veri çekme ve Redis'e kaydetme için:
  `python app.py`

Flask API'yi başlatmak için:
  `python flaskApı.py`

API çalıştıktan sonra:
 http://localhost:5000/scores  adresinden canlı skorları JSON formatında alabilirsiniz.


## API Kullanımı
GET /scores: Canlı skorları ve hesaplanan 2.5 üst, karşılıklı gol, kazanan bilgilerini JSON formatında döndürür.
 
 Örnek yanıt;
```
  "live_scores": 
    {
      "25_upper": false,
      "current_winner": 0,
      "home": "Inter Turku",
      "home_score": 0,
      "mutual_goal": false,
      "visitor": "AC Oulu",
      "visitor_score": 0
    }
```


## Docker Desteği
Proje, Docker ile konteynerleştirilmiştir.

API için:

  `docker build -f dockerfile-api -t match-score-api .`
  `docker run -p 5000:5000 match-score-api`
--
Veri çekme işlemi için:

  `docker build -f dockerfile-fetcher -t match-score-fetcher .`
  `docker run match-score-fetcher`
--
Docker Compose kullanarak her iki servisi birlikte başlatmak için:

  `docker-compose up`


## Swagger Desteği
Projede Swagger kullanılarak API dokümantasyonu oluşturulmuştur.
Dokümantasyon dosyası: static/swagger.yaml

Flask uygulaması çalışırken tarayıcıdan erişebilirsiniz: 
 http://localhost:5000/swagger

Swagger UI sayesinde API endpointlerini görsel olarak inceleyebilir ve test edebilirsiniz.


## Dosya Yapısı :
```
match-score/
├── static/
│   └── swagger.yaml      # Swagger API dokümantasyon dosyası
├── .dockerignore         # Docker build için yoksayılacak dosyalar
├── .env                  # API anahtarının ve diğer ortam değişkenlerinin saklandığı dosya
├── .gitignore            # Git tarafından izlenmeyecek dosyalar
├── app.py                # Veri çekme ve Redis'e kaydetme işlemlerini yönetir
├── flaskAPI.py           # Flask API sunucusu
├── docker-compose.yml    # Docker Compose yapılandırma dosyası
├── Dockerfile-api        # API servisi için Dockerfile
├── Dockerfile-fetcher    # Veri çekme servisi için Dockerfile
├── README.md             # Proje hakkında genel bilgiler
├── readscores.py         # Orijinal skor verisini çeken Python kodu (ihtiyaca göre)
└── requirements.txt      # Python bağımlılıklarını listeler
```
