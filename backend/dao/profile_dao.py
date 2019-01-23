from common.conexao import get_conexao
from model.profile import Profile
from model.usuario import Usuario

class ProfileDao(object):
    def __init__(self, conn, usuario):
        self.conn = conn
        self.usuario = usuario

    def novo(self, rs):
        return Profile(self.usuario, rs[0], rs[1])


    def obter_profile(self):
        sql = "select count(1) as quantidade , coalesce(sum(a.tamanho),0) as tamanho from ged.arquivos a where a.usuario_id = {}".format(self.usuario.get_id())
        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()

        user = self.novo(rs)

        cursor.close()

        return user
