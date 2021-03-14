"""
Create a URL shortening service. You may use the starter code provided here.
The app should have 2 endpoints:
 - One for creating short URLs from long ones
 - Another to take users who access short URLs that were shared with them to their final destination(long url).
A minimal solution without using a database is acceptable.
BONUS:
    - Add a database
    - Optimize short URL format
    - Add a simple UI
"""

import json
from flask import Flask, request, redirect
app = Flask(__name__)


data = {}

def load_json():
    global data
    with open('GHG-emissions-by-life-cycle-stage-OurWorldinData-upload.json', 'r') as f:
        data = json.load(f)
    if data:
        print('json loaded successfully!')
    else:
        print('uh oh, config is empty/ not loaded?')


@app.route('/emissions/<food>')
def get_emissions(food):
    return str(data[food]["total"])

@app.route('/data')
def get_all_data():
    return data

@app.route('/available_foods')
def get_avail_foods():
    avail_foods = []
    for food in data:
        avail_foods.append(food)
    return {"foods":avail_foods}



if __name__ == '__main__':
    load_json()
    app.run()