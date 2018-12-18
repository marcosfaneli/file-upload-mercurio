# -*- coding: utf-8 -*-
from flask import jsonify, request
from datetime import datetime, timedelta
import string

users = []

def check_authorization(f):
    def wrapper(*args, **kwargs):
        try:
            token = request.headers.get('Authorization')

            session = User()

            itens = token.split('.')

            user = session.encontrar_user(itens[0])
            if not user:
                raise Exception('User not found')

            if not session.validar_user(user, itens[1]):
                raise Exception('User invalid')

            return f(*args, **kwargs)
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "User invalid"}), 401

    return wrapper

class User(object):

    def __init__(self):
        pass


    def remover_user(self, email):
        index = 0
        for user in self.users:
            if user['email'] == email:
                users.pop(index)
                return True
            index += 1

        return True


    def encontrar_user(self, email):
        for user in users:
            if user['email'] == email:
                return user


    def nova_data_expiracao(self):
        agora = datetime.now()
        horas = timedelta(hours=1)
        expira = str(agora + horas)

        return expira


    def gerar_token(self, email, password):
        return '{}.{}'.format(email , password)


    def validar_user(self, user, password):
        if user['password'] == password:
            token = self.gerar_token(user['email'] , user['password'])
            user['expira'] = self.nova_data_expiracao()
            user['token'] = token

            return True
        else:
            return False

    @check_authorization
    def listar(self):
        return jsonify(users)


    @check_authorization
    def logout(self, request):
        try:
            remover_user(request.json['email'])
        except:
            return jsonify({'success': False, 'message': "User invalid"}), 401
        else:
            return jsonify({'success': True}), 200


    @check_authorization
    def status(self):
        return jsonify({'success': True}), 200


    def register(self, request):
        try:
            email = request.json['email']
            password = request.json['password']
            expira = self.nova_data_expiracao()
            token = self.gerar_token(request.json['email'] , request.json['password'])

            user = {'email': email,
                    'password': password,
                    'expira': expira,
                    'token': token}

            users.append(user)

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "User invalid"}), 401
        else:
            return jsonify({'success': True, 'token': token}), 200;


    def login(self, request):
        try:
            user = self.encontrar_user(request.json['email'])

            if not self.validar_user(user, request.json['password']):
              raise Exception('User invalid')

            user['expira'] = self.nova_data_expiracao()
            token = self.gerar_token(request.json['email'] , request.json['password'])
            user['token'] = token

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "User invalid"}), 401
        else:
            return jsonify({'success': True, 'token': token}), 200

#
# def find_session(email):
#     for session in sessions:
#         if session['email'] == email:
#             return session
#
# def validate_session(user, password):
#     if user['password'] == password:
#         token = make_token(user['email'] , user['password'])
#         user['expira'] = nova_data_expiracao()
#         user['token'] = token
#
#         return True
#     else:
#         return False
#
#
# def make_token(email, password):
#     _now = datetime.now()
#     _hour = timedelta(hours=1)
#     _expiration = str(_now + _hour)
#
#     return '{}.{}.{}'.format(email , password, _expiration)
#
#
# def check_authorization(f):
#     def wrapper(*args, **kwargs):
#         try:
#             token = request.headers.get('Authorization')
#             itens = token.split('.')
#
#             session = find_session(itens[0])
#
#             if not user:
#                 raise Exception('User not found')
#
#             if not validate_session(session, itens[1]):
#                 raise Exception('User invalid')
#
#             return f(*args, **kwargs)
#
#         except Exception as ex:
#             print(ex)
#             return jsonify({'success': False, 'message': "User invalid"}), 401
#
#     return wrapper
