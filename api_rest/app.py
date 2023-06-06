import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon')
def get_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon'
    limit = 100
    offset = 0
    params = {'limit': limit, 'offset': offset}

    response = requests.get(url, params=params)
    data = response.json()

    return jsonify(data['results'])

if __name__ == '__main__':
    app.run(port=5001)