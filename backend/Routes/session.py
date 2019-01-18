# -*- coding: utf-8 -*-
from flask import jsonify, request
from datetime import datetime, timedelta
import string
import jwt
from dao.empresa_dao import EmpresaDao
from dao.usuario_dao import UsuarioDao
from common.conexao import get_conexao
from common.config import KEY


users = []


def check_authorization(f):
    def wrapper(*args, **kwargs):
        try:
            authorization = request.headers.get('Authorization')

            token = jwt.decode(authorization, KEY, algorithms=['HS256'])

            session = Session()

            user = session.encontrar_sessao_aberta(token['user'], token['cnpj'])
            if not user:
                raise Exception('User not found')

            if not session.validar_user(user, token):
                raise Exception('User invalid')

            return f(*args, **kwargs)

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': ex.args}), 401

    return wrapper


class Session(object):

    def __init__(self):
        pass


    def remover_user(self, email, cnpj):
        index = 0
        for user in users:
            if user.get_email() == email and user.get_empresa().get_cnpj() == cnpj:
                users.pop(index)
                return True
            index += 1

        return True


    def encontrar_sessao_aberta(self, email, cnpj):
        for user in users:
            if user.get_email() == email and user.get_empresa().get_cnpj() == cnpj:
                return user


    def nova_data_expiracao(self):
        agora = datetime.now()
        horas = timedelta(hours=1)
        expira = str(agora + horas)

        return expira


    def gerar_token(self, email, password, cnpj):
        encoded = jwt.encode({'user': email, 'password': password, 'cnpj': cnpj}, KEY, algorithm='HS256')

        token = str(encoded)[2:-1]

        return token


    def validar_user(self, user, request):
        return user.get_senha() == request['password']


    @check_authorization
    def listar(self):
        return jsonify(users)


    def logout(self, request):
        try:
            authorization = request.headers.get('Authorization')

            token = jwt.decode(authorization, KEY, algorithms=['HS256'])

            self.remover_user(token['user'], token['cnpj'])
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': ex.args}), 200
        else:
            return jsonify({'success': True}), 200


    @check_authorization
    def status(self):
        return jsonify({'success': True}), 200


    def register(self, request):
        try:
            email = request.json['email']
            password = request.json['senha']
            cnpj = request.json['cnpj']
            nome = request.json['nome']

            user = {'email': email, 'password': password, 'cnpj': cnpj, 'nome': nome}

            users.append(user)

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "User invalid"}), 401
        else:
            return jsonify({'success': True}), 200;


    def login(self, request):
        empresa = ''

        try:
            empresa = request.json['empresa']
            if not empresa:
                raise Exception('Empresa não informada')
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "Empresa não informada"}), 401

        try:
            user = self.encontrar_user(request.json['email'], empresa)

            if not self.validar_user(user, request.json):
                raise Exception('User invalid')

            token = self.gerar_token(user.get_email() , user.get_senha(), user.get_empresa().get_cnpj())

            users.append(user)

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "User invalid"}), 401
        else:
            return jsonify({'success': True, 'token': token}), 200


    def encontrar_user(self, email, empresa):
        conn = get_conexao()
        empresa = EmpresaDao(conn).obter_pelo_alias(empresa)
        user = UsuarioDao(conn, empresa).obter_pelo_email(email)
        conn.close()

        return user
