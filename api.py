import json
from flask import Flask, jsonify, request
from flasgger import Swagger
from Controller.mainController import SplineController
import requests
from Database.database import Database
from flask_wtf.csrf import CSRFProtect

class TemperatureAPI:
    def __init__(self):
        self.app = Flask(__name__)
        self.csrf = CSRFProtect()
        self.db = Database('localhost', 'root', '', 'invernadero')
        self.swagger_config = {
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
            self.template = json.load(f)

        self.swagger = Swagger(self.app, config=self.swagger_config, template=self.template)

        self.controller = SplineController()
        self.stored_data = None

        self.csrf.init_app(self.app)

        self.app.route('/api/temperature', methods=['POST'])(self.get_temperature)
        self.app.route('/api/stored_temperature', methods=['GET'])(self.get_stored_temperature)

    def run(self):
        self.app.run(debug=True)

    def get_temperature(self):
        input_data = request.json
        time_values = input_data['time_values']
        temperature_values = input_data['temperature_values']
        time_points = input_data['time_points']

        result = self.controller.find_temperatures(time_values, temperature_values, time_points)

        self.stored_data = result.tolist()
        for i in range(len(time_points)):
            self.db.insert_temperature(time_points[i], self.stored_data[i])
        return jsonify({"temperature": self.stored_data})

    def get_stored_temperature(self):
        # Make a request to the other API to get the temperature data
        response = requests.post('http://127.0.0.1:5000/api/temperature', json={
            'time_values': [1, 2, 3, 4],
            'temperature_values': [10, 20, 30, 40],
            'time_points': [1.5, 2.5, 3.5]
        })

        if response.status_code != 200:
            return jsonify({"error": "Failed to retrieve temperature data from other API"}), response.status_code

        self.stored_data = response.json()['temperature']

        if self.stored_data is None:
            return jsonify({"error": "No data available"}), 404

        return jsonify({"temperature": self.stored_data})


if __name__ == '__main__':
    api = TemperatureAPI()
    api.run()
