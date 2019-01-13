from conexao import get_conexao
from empresa import Empresa
from usuario import Usuario

class UsuarioDao(object):
    def __init__(self, conn, empresa):
        self.conn = conn
        self.empresa = empresa

    def novo(self, rs):
        return Usuario(self.empresa, rs[0], rs[1], rs[2], rs[3])


    def obter_pelo_email(self, email):
        sql = "select u.id, u.nome, u.email, u.senha from acesso.usuarios u where u.email = '{}' and u.empresa_id = {}".format(email, self.empresa.get_id())
        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()

        user = self.novo(rs)

        cursor.close()

        return user
