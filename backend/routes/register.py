import os
from flask import jsonify, request
from common.conexao import get_conexao
from routes.session import check_authorization
from dao.register_dao import RegisterDAO
from model.solicitacao import Solicitacao
from model.usuario import Usuario

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

            register = RegisterDAO(conn, solicitacao).new()
            conn.close()
                        

        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': str(ex)}), 401
        else:
            return jsonify({'success': True, 'id_solicitacao': register.get_id()}), 200;    
    
    def accept_register(self):
        try:
            conn = get_conexao()

            id = self.request.json['id']

            usuario = RegisterDAO(conn, None).buscarSolicitacao(id)

            if (usuario.get_nome == ''):
                raise Exception("Nenhuma solicitação encontrada para o ID: '{}'.".format(id))
            else:
                id_usuario = RegisterDAO(conn, None).aprovar_registro(usuario)
                RegisterDAO(conn, None).excluir_solicitacao(id)

            
        except Exception as ex:
            return jsonify({'success': False, 'message': str(ex)}), 401
        else:
            return jsonify({'success': True, 'id_usuario': id_usuario}), 200;        
        

    