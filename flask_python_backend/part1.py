import json
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/v1/', methods=['GET'])
def getdata():
    
    # GET a json response
    if request.method == 'GET':
        data = {
                "message": "Bem vindo a API GeoPoly!"
            }
        return jsonify(data), 200

@app.route('/v1/auth/', methods=['POST'])
def login():
    
    # POST credentials for authentication (Not actual auth)
    if request.method == 'POST':
        info = json.loads(request.data)
        email = info.get('email')
        password = info.get('password')
        if email == "admin@exemplo.com.br" and password == "abcd1234":
            data = {
                    "message": "Autenticado com sucesso!"
                }
            return jsonify(data), 200
        else:
            data = {
                    "message": "Falha ao autenticar!"
                }
            return jsonify(data), 401



if __name__ == '__main__':
    app.debug = False
        
    app.run()
