from flask import request
from empresa_dao import EmpresaDao
from usuario_dao import UsuarioDao
from conexao import get_conexao
import jwt
from config import KEY


class UsuarioLogado(object):
    def __init__(self):
        pass

    def identificar_usuario_token(self, chave):
        token = jwt.decode(chave, KEY, algorithms=['HS256'])

        return self.__encontrar_user(token['user'], token['cnpj'])

    def identificar_usuario(self, request):
        authorization = request.headers.get('Authorization')
        token = jwt.decode(authorization, KEY, algorithms=['HS256'])

        return self.__encontrar_user(token['user'], token['cnpj'])

    def __encontrar_user(self, email, cnpj):
        conn = get_conexao()
        empresa = EmpresaDao(conn).obter_pelo_cnpj(cnpj)
        user = UsuarioDao(conn, empresa).obter_pelo_email(email)
        conn.close()

        return user
