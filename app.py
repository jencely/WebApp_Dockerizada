from flask import Flask, render_template, jsonify
import requests
import os
import base64

app = Flask(__name__)

API_KEY = "acc_78c6aed24bbb0e9"
API_SECRET = "24c2beda6ea48b93a1d13a45428a84b7"
API_ENDPOINT = "https://api.imagga.com/v2/tags"

#magenes de prueba
IMAGES = [
    "/static/images/paisaje.jpg",
    "/static/images/gatito.jpg",
    "/static/images/cerveza.jpg"
]

@app.route('/')
def index():
    return render_template('index.html', images=IMAGES)

@app.route('/analyze/<filename>')
def analyze(filename):
    image_path = os.path.join('static', 'images', filename)
    
    try:
        response = requests.post(
            API_ENDPOINT,
            auth=(API_KEY, API_SECRET),
            files={'image': open(image_path, 'rb')}
        )
        
        if response.status_code == 200:
            tags = response.json()['result']['tags'][:2]
            return jsonify(tags)
        
        return jsonify({'error': response.text}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000, debug=True)
    
