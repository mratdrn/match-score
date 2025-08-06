import requests
import redis
import time

# Redis bağlantısı
r = redis.Redis(host='localhost', port=6379, db=0)

API_KEY = "98bc6887cb868bf41ec78bb242a2e75e"
API_URL = "https://v3.football.api-sports.io/fixtures?live=all"

headers = {
    "x-apisports-key": API_KEY
}

def fetch_and_store():
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        data = response.text  # JSON string olarak alıyorum

        # Redis'e kaydet
        r.set("live_scores", data)

        print(f"Veri güncellendi: {time.ctime()}")
    except Exception as e:
        print("Hata:", e)

if __name__ == "__main__":
    while True:
        fetch_and_store()
        time.sleep(900)  # Günlük 100 istek hakkımız var 
        

