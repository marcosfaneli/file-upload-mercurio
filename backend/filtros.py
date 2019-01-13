from flask import jsonify, request
from session import check_authorization
from conexao import get_conexao
from usuario_logado import UsuarioLogado
from categoria_dao import CategoriaDao


class Filtros(object):
    def __init__(self, request):
        self.request = request

    def __novo(self, categoria):
        return {'id': categoria.get_id(), 'descricao': categoria.get_nome(), 'cor': categoria.get_cor()}

    @check_authorization
    def categorias(self):
        try:
            conn = get_conexao()
            usuario  = UsuarioLogado().identificar_usuario(request)
            categorias = CategoriaDao(conn, usuario).listar()

            lista = []

            for categoria in categorias:
                lista.append(self.__novo(categoria))

            conn.close()
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "Error listing"}), 404
        else:
            return jsonify({'success': True, 'categorias': lista}), 200
