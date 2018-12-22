from flask import jsonify, request
from session import User, check_authorization


class Categoria(object):
    def __init__(self):
        pass

    @check_authorization
    def listar(self):
        try:
            categorias = [
                {'id': 1, 'descricao': "Teste", 'cor': "#fefefe"},
                {'id': 2, 'descricao': "Outros", 'cor': "#fefafa"}
            ]
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "Error listing"}), 404
        else:
            return jsonify({'success': True, 'categorias': categorias}), 200
