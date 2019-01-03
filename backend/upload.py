from session import User, check_authorization
import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename


class Upload(object):
    def __init__(self):
        self.UPLOAD_FOLDER = 'c:/temp/'
        self.ALLOWED_EXTENSIONS = set(['txt', 'doc', 'docx', 'xls', 'xlsx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS


    @check_authorization
    def carregar(self, request):
        try:
            if 'arquivo' not in request.files:
                raise Exception('Não há arquivo')

            print(request.form['descricao'])
            print(request.form['chave'])
            print(request.form['categoria'])

            file = request.files['arquivo']

            if file.filename == '':
                raise Exception('Tipo de arquivo invalido')

            if file and self.allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(self.UPLOAD_FOLDER, filename))
            else:
                raise Exception('Extensão não permitida')

            id = 1

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': ex.args}), 200
        else:
            return jsonify({'success': True, 'id': id}), 200
