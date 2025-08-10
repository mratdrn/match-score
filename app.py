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

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD") or None

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    db=0,
    decode_responses=True
)


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
        

