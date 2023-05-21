import json
import os
import sys
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/v3/places', methods=['GET', 'POST'])
def getpostplaces():
    
    # GET places list from file
    if request.method == 'GET':
        data = json.load(open(os.path.join(sys.path[0], "places.json"), "r"))
        return jsonify(data), 200
    
    # POST new place
    if request.method == 'POST':
        new_info = json.loads(request.data)
        file = open(os.path.join(sys.path[0], "places.json"), "r")
        data = json.load(file)
        try:
            new_place = {
                        "id": len(data)+1,
                        "name": new_info["name"],
                        "latitude": new_info["latitude"],
                        "longitude": new_info["longitude"]
                        }
            data.append(new_place)
            file.close()
            json.dump(data, open(os.path.join(sys.path[0], "places.json"), "w"))
            return jsonify(new_place), 200
        except Exception as error:
            print(error)
            return jsonify("It wasn't possible to add new place"), 500

@app.route('/v3/places/<string:id>', methods=['GET', 'PUT'])
def getputuniqueplace(id):
    
    # GET specific place
    if request.method == 'GET':
        info = json.load(open(os.path.join(sys.path[0], "places.json"), "r"))
        for i in info:
            if i.get('id') == int(id):
                return jsonify(i), 200
        return jsonify('No place found!'), 500
    
    # PUT specific place
    if request.method == 'PUT':
        new_info = json.loads(request.data)
        file = open(os.path.join(sys.path[0], "places.json"), "r")
        info = json.load(file)
        for i in info:
            if i.get('id') == int(id):
                try:
                    new_place = {
                        "id": int(id),
                        "name": new_info["name"],
                        "latitude": new_info["latitude"],
                        "longitude": new_info["longitude"]
                        }
                    info[int(id)-1] = new_place
                    file.close()
                    json.dump(info, open(os.path.join(sys.path[0], "places.json"), "w"))
                    return jsonify(new_place), 200
                except Exception as error:
                    print(error)
                    return jsonify("It wasn't possible to add new place"), 500
        return jsonify('No place found!'), 500


if __name__ == '__main__':
    app.debug = False
        
    app.run()
