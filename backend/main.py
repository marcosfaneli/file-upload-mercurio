# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS
from session import User
from upload import upload_file


app = Flask(__name__)
cors = CORS(app, resources = {r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def listar():
    return User().listar()

@app.route('/auth/logout', methods=['GET'])
def logout():
    return User().logout(request)

@app.route('/auth/status', methods=['GET'])
def status():
    return User().status()

@app.route('/auth/register', methods=['POST'])
def register():
    return User().register(request)

@app.route('/auth/login', methods=['POST'])
def login():
    return User().login(request)

@app.route('/upload', methods=['POST'])
def upload():
    return upload_file(request)

app.run(debug=True, host='100.0.66.160')
