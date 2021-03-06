from routes.session import check_authorization
import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from common.conexao import get_conexao
from model.arquivo import Arquivo
from common.usuario_logado import UsuarioLogado
from dao.categoria_dao import CategoriaDao
from dao.arquivo_dao import ArquivoDao
from common.config import UPLOAD_FOLDER


class Upload(object):
    def __init__(self):
        self.ALLOWED_EXTENSIONS = set(['txt', 'doc', 'docx', 'xls', 'xlsx', 'pdf', 'png', 'jpg', 'jpeg', 'zip'])


    def __allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS


    @check_authorization
    def carregar(self, request):
        try:
            if 'arquivo' not in request.files:
                raise Exception('Não há arquivo')

            file = request.files['arquivo']

            if file.filename == '':
                raise Exception('Tipo de arquivo invalido')

            if file and self.__allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
            else:
                raise Exception('Extensão não permitida')

            id = self.__inserir(request)

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': ex.args}), 500
        else:
            return jsonify({'success': True, 'id': id}), 200


    def __inserir(self, request):
        conn = get_conexao()

        usuario = UsuarioLogado().identificar_usuario(request)

        keys = request.form['chave'].split(";")

        categoria = request.form['categoria']
        categoria = CategoriaDao(conn, usuario).obter_pelo_id(categoria)

        file = request.files['arquivo']
        tipo = file.filename.rsplit('.', 1)[1]
        tamanho = os.path.getsize ('{}/{}'.format(UPLOAD_FOLDER, file.filename))
        print(tamanho)
        tamanho = tamanho / 1024 / 1024

        arquivo = Arquivo(request.form['descricao'], categoria, keys, tipo, '', usuario, file.filename, tamanho, 0)
        id = ArquivoDao(conn, usuario).adicionar(arquivo)
        conn.close()

        return id
