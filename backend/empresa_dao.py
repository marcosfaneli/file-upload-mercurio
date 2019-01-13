from conexao import get_conexao
from empresa import Empresa

class EmpresaDao:
    def __init__(self, conn):
        self.conn = conn

    def __novo(self, rs):
        return Empresa(rs[1], rs[2], rs[0], rs[3])


    def obter_pelo_cnpj(self, cnpj):
        sql = "select e.id, e.cnpj, e.nome, e.alias from acesso.empresas e where e.cnpj = '{}'".format(cnpj)
        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()

        empresa = self.__novo(rs)

        cursor.close()

        return empresa


    def obter_pelo_alias(self, alias):
        sql = "select e.id, e.cnpj, e.nome, e.alias from acesso.empresas e where e.alias = '{}'".format(alias)
        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()

        empresa = self.__novo(rs)

        cursor.close()

        return empresa


    def obter_pelo_id(self, id):
        sql = "select e.id, e.cnpj, e.nome, e.alias from acesso.empresas e where e.id = '{}'".format(id)
        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()

        empresa = self.__novo(rs)

        cursor.close()

        return empresa
