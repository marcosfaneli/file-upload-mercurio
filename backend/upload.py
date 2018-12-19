import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = 'c:/temp/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file(request):
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
        return jsonify({'success': True}), 401
    else:
        return jsonify({'success': True}), 200