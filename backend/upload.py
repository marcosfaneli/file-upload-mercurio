from session import User, check_authorization
import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename


class Upload(object):
    UPLOAD_FOLDER = 'c:/temp/'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @check_authorization
    def carregar(request):
        try:
            print('chegou')
            print(request.files)

            if 'file' not in request.files:
                return jsonify({'success': True}), 401

            file = request.files['file']
            print(file)

            if file.filename == '':
                return jsonify({'success': True}), 401

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))

        except Exception as ex:
            print(ex)
            return jsonify({'success': False}), 404
        else:
            return jsonify({'success': True}), 200
