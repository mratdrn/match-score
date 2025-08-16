from flask import Flask, jsonify
import redis
import json
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Swagger UI ayarları 
SWAGGER_URL = '/swagger'  # Swagger UI'yi bu path'ten serve edeceğiz
API_URL = '/static/swagger.yaml'  # swagger.yaml dosyanın yolu (Flask static klasöründe olmalı)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Live Match Scores API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
