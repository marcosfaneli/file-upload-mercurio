import os
from flask import jsonify, request
from common.conexao import get_conexao
from routes.session import check_authorization
from dao.register_dao import RegisterDAO
from model.solicitacao import Solicitacao

class Register(object):
    def __init__(self, request):
        self.request = request

    def register(self):
        try:
            email = self.request.json['email']
            password = self.request.json['senha']
            cnpj = self.request.json['cnpj']
            nome =self. request.json['nome']        

            solicitacao = Solicitacao(0, email, cnpj, password, nome)
            conn = get_conexao()
        
            register = RegisterDAO(conn, solicitacao).verificarSolicitacao()

            if (register.get_id() != ''):
                raise Exception("Já existe uma solicitação para o email: '{}'".format(register.get_email()))

            register =RegisterDAO(conn, solicitacao).new()
            conn.close()
                        

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': str(ex)}), 401
        else:
            return jsonify({'success': True, 'id_solicitacao': register.get_id()}), 200;    

    