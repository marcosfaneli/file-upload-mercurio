# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS
from session import User
from categoria import Categoria
from upload import Upload
from arquivo import Arquivo


app = Flask(__name__)
cors = CORS(app, resources = {r"/*": {"origins": "*"}})


@app.route('/recente', methods=['GET'])
def recente():
    return Arquivo().recente()

@app.route('/pesquisa/<texto>', methods=['GET'])
def pesquisa(texto):
    return Arquivo().pesquisa(texto)

@app.route('/detail/<id>', methods=['GET'])
def detalhes(id):
    return Arquivo().detalhes(id)

@app.route('/auth/logout', methods=['GET'])
def logout():
    return User().logout(request)

@app.route('/status', methods=['GET'])
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
    return Upload().carregar(request)

@app.route('/categoria', methods=['GET'])
def listar_categoria():
    return Categoria().listar()

@app.route('/', methods=['GET'])
def teste():
    return 'online', 200;

app.run(debug=True)
