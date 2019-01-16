from session import check_authorization
import os
from flask import Flask, flash, request, redirect, url_for, jsonify, current_app, send_from_directory
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER
from conexao import get_conexao
from usuario_logado import UsuarioLogado
from arquivo_dao import ArquivoDao
from arquivo import Arquivo


class Download(object):
    def __init__(self, token):
        self.token = token


    def download(self, id):
        try:
            conn = get_conexao()
            user = UsuarioLogado().identificar_usuario_token(self.token)
            arquivo = ArquivoDao(conn, user).obter(id)

            filename = arquivo.get_arquivo()
            print(filename)
            # filename = 'Mapa_de_acao.pdf'
            uploads = os.path.join(current_app.root_path, UPLOAD_FOLDER)
            return send_from_directory(directory=uploads, filename=filename)

            conn.close()
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "File not found"}), 500
        else:
            return jsonify({'success': True, 'arquivo': item}), 200
