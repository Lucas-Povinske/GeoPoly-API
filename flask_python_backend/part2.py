import json
import os
import sys
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = [
        {
        "id": 1,
        "name": "Parque da Cidade",
        "latitude": -23.221112,
        "longitude": -45.899678
        },
        {
        "id": 2,
        "name": "Praca Ulisses Guimaraes",
        "latitude": -23.180038,
        "longitude": -45.884357
        },
        {
        "id": 3,
        "name": "Pocos de Caldas",
        "latitude": -46.579163362267565,
        "longitude": -21.786744715480665
        },
        {
        "id": 4,
        "name": "Bauru",
        "latitude": -49.079598138133946,
        "longitude": -22.30546088985504
        },
        {
        "id": 5,
        "name": "Paris",
        "latitude": 2.3804215232722186,
        "longitude": 48.904321741758196
        },
        {
        "id": 6,
        "name": "Dublin",
        "latitude": -6.270931684537629,
        "longitude": 53.37368589499894
        }
    ]

@app.route('/v2/places', methods=['GET'])
def getplaces():
    
    # GET places list
    if request.method == 'GET':
        return jsonify(data), 200

@app.route('/v2/places/<string:id>', methods=['GET'])
def getuniqueplace(id):
    
    # GET specific place
    if request.method == 'GET':
        info = data
        for i in info:
            if i.get('id') == int(id):
                return jsonify(i), 200
        return jsonify('No place found!'), 500



if __name__ == '__main__':
    app.debug = False
        
    app.run()
