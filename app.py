import requests
import redis
import time


from dotenv import load_dotenv
import os

load_dotenv()  # .env dosyasını yükler

API_KEY = os.getenv("API_KEY")
DEBUG = os.getenv("DEBUG")
API_URL = os.getenv("API_URL")

print("API Key:", API_KEY)
print("Debug modu:", DEBUG)


# Redis bağlantısı
r = redis.Redis(host='localhost', port=6379, db=0)

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
        

