from session import User, check_authorization
import os
from flask import Flask, flash, request, redirect, url_for, jsonify, current_app, send_from_directory
from werkzeug.utils import secure_filename


class Download(object):
    def __init__(self):
        self.UPLOAD_FOLDER = 'c:/temp/'

    def download(self, id):
        filename = 'Mapa_de_acao.pdf'
        uploads = os.path.join(current_app.root_path, self.UPLOAD_FOLDER)
        return send_from_directory(directory=uploads, filename=filename)
