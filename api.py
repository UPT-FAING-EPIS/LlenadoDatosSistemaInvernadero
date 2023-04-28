import json
from flask import Flask, jsonify, request
from flasgger import Swagger
from Controller.mainController import SplineController
import requests
from Database.database import Database
from flask_wtf.csrf import CSRFProtect
db = Database('localhost', 'root', '', 'invernadero')

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
}

with open("swagger_template.json", "r") as f:
    template = json.load(f)

swagger = Swagger(app, config=swagger_config, template=template)

controller = SplineController()
stored_data = None

@app.route('/api/temperature', methods=['POST'])
def get_temperature():
    
    input_data = request.json
    time_values = input_data['time_values']
    temperature_values = input_data['temperature_values']
    time_points = input_data['time_points']

    result = controller.find_temperatures(time_values, temperature_values, time_points)

    
    stored_data = result.tolist()
    for i in range(len(time_points)):
      
        db.insert_temperature(time_points[i], stored_data[i])
    return jsonify({"temperature": stored_data})


@app.route('/api/stored_temperature', methods=['GET'])
def get_stored_temperature():
    global stored_data

    # Make a request to the other API to get the temperature data
    response = requests.post('http://127.0.0.1:5000/api/temperature', json={
        'time_values': [1, 2, 3, 4],
        'temperature_values': [10, 20, 30, 40],
        'time_points': [1.5, 2.5, 3.5]
    })

    if response.status_code != 200:
        return jsonify({"error": "Failed to retrieve temperature data from other API"}), response.status_code

    stored_data = response.json()['temperature']

    if stored_data is None:
        return jsonify({"error": "No data available"}), 404

    return jsonify({"temperature": stored_data})
if __name__ == '__main__':
    app.run(debug=True)
