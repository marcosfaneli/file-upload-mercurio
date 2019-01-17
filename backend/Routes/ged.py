from flask import jsonify, request
from DAO.arquivo_dao import ArquivoDao
from Common.usuario_logado import UsuarioLogado
from Common.conexao import get_conexao
from Routes.session import check_authorization


class Ged(object):
    def __init__(self, request):
        self.request = request

    @check_authorization
    def detalhes(self, id):
        try:
            conn = get_conexao()
            user = UsuarioLogado().identificar_usuario(self.request)
            arquivo = ArquivoDao(conn, user).obter(id)

            item = self.__novo_item(arquivo)

            conn.close()
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "File not found"}), 500
        else:
            return jsonify({'success': True, 'arquivo': item}), 200


    @check_authorization
    def recente(self):
        try:
            conn = get_conexao()
            user = UsuarioLogado().identificar_usuario(self.request)
            arquivos = ArquivoDao(conn, user).listar()

            lista = []

            for arquivo in arquivos:
                lista.append(self.__novo_item(arquivo))

            conn.close()
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "Error listing"}), 500
        else:
            return jsonify({'success': True, 'arquivos': lista}), 200


    def __novo_item(self, item):
        categoria = {
                     'nome': item.get_categoria().get_nome(),
                     'cor': item.get_categoria().get_cor(),
                     'id': item.get_categoria().get_id()
                    }

        visualizadores = [{'nome': item.get_usuario_postou().get_nome(), 'data': item.get_data_postado()}]

        arquivo = {
                   'descricao': item.get_descricao(),
                   'categoria': categoria,
                   'keys': item.get_keys(),
                   'tipo': item.get_tipo(),
                   'usuario_postou': item.get_usuario_postou().get_nome(),
                   'data_postado': item.get_data_postado(),
                   'visualizadores': visualizadores,
                   'classificacao': item.get_classificacao(),
                   'url': item.get_url(),
                   'id': item.get_id()
                  }

        return arquivo


    @check_authorization
    def pesquisa(self, texto):
        try:
            conn = get_conexao()
            user = UsuarioLogado().identificar_usuario(self.request)
            arquivos = ArquivoDao(conn, user).pesquisar(texto)

            lista = []

            for arquivo in arquivos:
                lista.append(self.__novo_item(arquivo))

            conn.close()
        except Exception as ex:
            print(ex)
            return jsonify({'success': False, 'message': "Error listing"}), 500
        else:
            return jsonify({'success': True, 'arquivos': lista}), 200
