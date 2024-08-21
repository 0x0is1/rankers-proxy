from flask import Flask, request
import flask, requests
app = Flask(__name__)

BASE_URL = "https://api.ranker.com/"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def forwarding(path):
    url = BASE_URL + str(request.url).split('https://rankers-proxy.onrender.com/')[1]
    print(url)
    response = requests.get(url, stream=True).json()
    response = flask.jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
