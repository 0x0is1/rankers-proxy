from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BASE_URL = "https://api.ranker.com/"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def forwarding(path):
    url = f"{BASE_URL}{path}"
    
    response = requests.get(url, stream=True)
    
    response_json = response.json()
    response = jsonify(response_json)
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
