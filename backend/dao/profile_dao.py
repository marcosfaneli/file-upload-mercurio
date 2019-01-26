from common.conexao import get_conexao
from model.profile import Profile
from model.usuario import Usuario

class ProfileDao(object):
    def __init__(self, conn, usuario):
        self.conn = conn
        self.usuario = usuario

    def novo(self, rs):
        return Profile(self.usuario, rs[0], rs[1], rs[2])


    def obter_profile(self):
        sql = " select count(1) as quantidade , coalesce(sum(a.tamanho),0) as tamanho "
        sql += "       , (select count(1) from acesso.solicitacoes s where s.cnpj = e.cnpj) as solicitacoes "
        sql += "  from ged.arquivos a "
        sql += "  join acesso.empresas e on e.id = a.empresa_id "
        sql += " where a.usuario_id = {} group by e.cnpj ".format(self.usuario.get_id())

        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()

        user = self.novo(rs)

        cursor.close()

        return user
