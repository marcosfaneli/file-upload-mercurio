# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.session import Session
from routes.filtros import Filtros
from routes.upload import Upload
from routes.download import Download
from routes.ged import Ged
from routes.register import Register


app = Flask(__name__)
cors = CORS(app, resources = {r"/*": {"origins": "*"}})


@app.route('/recent', methods=['GET'])
def recente():
    return Ged(request).recente()

@app.route('/find/<texto>', methods=['GET'])
def pesquisa(texto):
    return Ged(request).pesquisa(texto)

@app.route('/detail/<id>', methods=['GET'])
def detalhes(id):
    return Ged(request).detalhes(id)

@app.route('/auth/logout', methods=['GET'])
def logout():
    return Session().logout(request)

@app.route('/status', methods=['GET'])
def status():
    return Session().status(request)

@app.route('/auth/register', methods=['POST'])
def register():
    return Register(request).register()

@app.route('/auth/login', methods=['POST'])
def login():
    return Session().login(request)

@app.route('/upload', methods=['POST'])
def upload():
    return Upload().carregar(request)

@app.route('/download/<token>/<id>', methods=['GET'])
def download(token, id):
    return Download(token).download(id)

@app.route('/categoria', methods=['GET'])
def listar_categoria():
    return Filtros(request).categorias()

@app.route('/', methods=['GET'])
def teste():
    return 'online', 200;

if __name__ == "__main__":
    app.run(debug=True)
