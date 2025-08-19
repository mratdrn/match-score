# Redis’teki canlı skor verisini Flask API ile tarayıcıya sunacağız.
# We will serve the live score data stored in Redis to the browser using a Flask API.

from flask import Flask, jsonify                      # Flask web framework’ünü ve JSON response döndüren jsonify fonksiyonunu import ediyoruz.
import redis                                          # Redis ile bağlantı kurmak için Python Redis kütüphanesi.
import json                                           # Python’un standart JSON kütüphanesi.
from flask_swagger_ui import get_swaggerui_blueprint  # Flask içinde swagger uı'yı serve etmek için kullanılır.

# Flask'i başlatıyoruz
app = Flask(__name__)        

# Redis bağlantısı
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Swagger UI ayarları 
SWAGGER_URL = '/swagger'  # Swagger uı'yı bu path'ten serve edeceğiz.
API_URL = '/static/swagger.yaml'  # swagger.yaml dosya yolu, static isimli ayrı dizine taşındı.

# Swagger uı blueprint oluşturuldu
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Live Match Scores API"
    }
)
# Swagger blueprint flask'a ekleniyor
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


# /scores endpoint’ini tanımladık böylece HTTP GET varsayılan olarak çalışır ve canlı maç skorlarını JSON formatında döndürür.
@app.route('/scores')                
def get_scores():
    data = r.get("live_scores")
    if not data:
        return jsonify({"error": "Veri bulunamadı"}), 404

    try:
        parsed = json.loads(data)
        response = {"live_scores": []}

        # API response verisindeki maçları dolaşacak 
        for match in parsed.get("response", []):
            home_team = match["teams"]["home"]["name"]
            away_team = match["teams"]["away"]["name"]
            home_score = match["goals"]["home"]
            away_score = match["goals"]["away"]

            total_goals = (home_score or 0) + (away_score or 0)
            upper_25 = total_goals > 2.5
            mutual_goal = (home_score or 0) > 0 and (away_score or 0) > 0

            if home_score == away_score:
                winner = 0
            elif home_score > away_score:
                winner = 1
            else:
                winner = 2

            response["live_scores"].append({
                "home": home_team,
                "visitor": away_team,
                "home_score": home_score,
                "visitor_score": away_score,
                "25_upper": upper_25,
                "mutual_goal": mutual_goal,
                "current_winner": winner
            })

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": "JSON parse hatası", "message": str(e)}), 500

# Flask'i 0.0.0.0:5000’te debug modunda çalıştırır.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# API endpoint URL’si
# http://127.0.0.1:5000/scores
# Redis’ten alınan canlı maç skorlarını JSON formatında döner.

# Swagger uı endpoint’i
# http://127.0.0.1:5000/swagger
# Swagger uı üzerinden API dokümantasyonunu görüp test edebilirsin.

# swagger.yaml dosyası
# http://127.0.0.1:5000/static/swagger.yaml
# Swagger uı'nın kullandığı YAML dosyası