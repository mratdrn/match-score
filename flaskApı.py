# Redis’teki canlı skor verisini Flask API ile tarayıcıya sunacağız.
# We will serve the live score data stored in Redis to the browser using a Flask API.

from flask import Flask, jsonify
import redis
import json

app = Flask(__name__)

# Redis bağlantısı
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/scores')
def get_scores():
    data = r.get("live_scores")
    if not data:
        return jsonify({"error": "Veri bulunamadı"}), 404
    try:
        parsed = json.loads(data)
        return jsonify(parsed)
    except Exception as e:
        return jsonify({"error": "JSON parse hatası", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
