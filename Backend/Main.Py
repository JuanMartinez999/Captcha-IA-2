from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

images = []
results = []

@app.route('/api/images')
def get_images():
    return jsonify(images)

@app.route('/api/save-result', methods=['POST'])
def save_result():
    data = request.json
    data['date'] = datetime.utcnow().isoformat()
    results.append(data)
    return jsonify({'status': 'ok'})

@app.route('/api/ranking')
def get_ranking():
    return jsonify(sorted(results, key=lambda x: x['correct'], reverse=True))

if __name__ == '__main__':
    app.run(debug=True)
