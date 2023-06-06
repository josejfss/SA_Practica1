from flask import Flask, render_template, jsonify
from zeep import Client
from zeep.helpers import serialize_object
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/countries')
def get_countries():
    wsdl = 'http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
    client = Client(wsdl)

    response = client.service.FullCountryInfoAllCountries()
    limited_response = response[:100]
    serialized_response = serialize_object(limited_response)
    json_string = json.dumps(serialized_response)
    json_object = json.loads(json_string)
    return json_object

if __name__ == '__main__':
    app.run()