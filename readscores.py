import redis
import json

# Redis bağlantısı
r = redis.Redis(host='localhost', port=6379, db=0)

def read_scores():
    data = r.get("live_scores")
    if data:
        try:
            parsed = json.loads(data)

            # JSON kodunun okunaklığı için;
            print(json.dumps(parsed, indent=2, ensure_ascii=False))
        except Exception as e:
            print("JSON parse hatası:", e) #500
    else:
        print("Redis'te canlı skor verisi bulunamadı.") #404

if __name__ == "__main__":
    read_scores()
