import json
import os
import sys
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
from flask_cors import CORS
import geopy.distance

app = Flask(__name__)
CORS(app)

@app.route('/v4/places/<string:id1>/distanceto/<string:id2>', methods=['GET'])
def getdistance(id1,id2):
    
    # GET distance between two places
    if request.method == 'GET':
        info = json.load(open(os.path.join(sys.path[0], "places.json"), "r"))
        for i in info:
            if i.get('id') == int(id1):
                firstplace = i
            elif i.get('id') == int(id2):
                secondplace = i
        if firstplace and secondplace:
            coords_1 = (firstplace["latitude"], firstplace["longitude"])
            coords_2 = (secondplace["latitude"], secondplace["longitude"])
            distance = geopy.distance.geodesic(coords_1, coords_2).km
            resp = {
                    "distance": distance
                }
            return jsonify(resp), 200
        return jsonify('Not all places were found!'), 500

@app.route('/v4/search', methods=['GET'])
def getplacesinradius():
    
    # GET all places in radius
    if request.method == 'GET':
        lat = request.args.get('latitude')
        long = request.args.get('longitude')
        rad = request.args.get('radius')
        info = json.load(open(os.path.join(sys.path[0], "places.json"), "r"))
        refcoord = (float(lat),float(long))
        resp = []
        for i in info:
            new_info = i
            coord = (i["latitude"], i["longitude"])
            print(refcoord)
            print(coord)
            distance = geopy.distance.geodesic(refcoord, coord).km
            print(distance)
            if distance < float(rad):
                new_info['distance'] = distance
                resp.append(new_info)
        if resp:
            return jsonify(resp), 200
        return jsonify('No places in radius!'), 200

if __name__ == '__main__':
    app.debug = False
        
    app.run()
