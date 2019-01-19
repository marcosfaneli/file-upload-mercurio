from model.categoria import Categoria

class CategoriaDao(object):
    def __init__(self, conn, usuario):
        self.conn = conn
        self.usuario = usuario


    def __novo(self, rs):
        return Categoria(rs[0], rs[2], rs[3])


    def listar(self):
        sql = "select id, empresa_id, descricao, cor from ged.categorias where empresa_id = {}".format(self.usuario.get_empresa().get_id())
        cursor = self.conn.cursor()
        cursor.execute(sql)

        ds = cursor.fetchall()

        categorias = []

        for rs in ds:
            categorias.append(self.__novo(rs))

        cursor.close()

        return categorias


    def obter_pelo_id(self, id):
        sql = "select id, empresa_id, descricao, cor from ged.categorias where id = {} and empresa_id = {}".format(id, self.usuario.get_empresa().get_id())
        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()

        categoria = self.__novo(rs)

        cursor.close()

        return categoria


    def obter_pela_descricao(self, descricao):
        sql = "select id, empresa_id, descricao, cor from ged.categorias where lower(descricao) = '{}' and empresa_id = {}".format(descricao.lower(), self.usuario.get_empresa().get_id())
        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()

        categoria = self.__novo(rs)

        cursor.close()

        return categoria
