# -*- coding: utf-8 -*-
from flask import jsonify, request
from datetime import datetime, timedelta
import string
import jwt


KEY = 'meupiru'


users = [{'email': "faneli", 'password': "123456"}]


def check_authorization(f):
    def wrapper(*args, **kwargs):
        try:
            authorization = request.headers.get('Authorization')

            token = jwt.decode(authorization, KEY, algorithms=['HS256'])

            session = User()

            user = session.encontrar_user(token['user'])
            if not user:
                raise Exception('User not found')

            if not session.validar_user(user, token['password']):
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
        for user in users:
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
        encoded = jwt.encode({'user': email, 'password': password}, KEY, algorithm='HS256')
        
        token = str(encoded)[2:-1]

        return token


    def validar_user(self, user, password):
        return user['password'] == password
        

    @check_authorization
    def listar(self):
        return jsonify(users)


    @check_authorization
    def logout(self, request):
        try:
            authorization = request.headers.get('Authorization')

            token = jwt.decode(authorization, KEY, algorithms=['HS256'])

            self.remover_user(token['user'])
        except Exception as ex:
            print(ex)
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

            user = {'email': email, 'password': password}

            users.append(user)

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "User invalid"}), 401
        else:
            return jsonify({'success': True}), 200;


    def login(self, request):
        try:
            print(request)
            user = self.encontrar_user(request.json['email'])

            if not self.validar_user(user, request.json['password']):
              raise Exception('User invalid')

            token = self.gerar_token(request.json['email'] , request.json['password'])

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "User invalid"}), 401
        else:
            return jsonify({'success': True, 'token': token}), 200
