from common.conexao import get_conexao
from model.solicitacao import Solicitacao
from model.usuario import Usuario
import datetime

class RegisterDAO(object):
    def __init__(self, conn, solicitacao):
        self.conn = conn
        self.solicitacao = solicitacao

    def new(self):

        sql = "insert into acesso.solicitacoes (id, email, cnpj, senha, nome)"
        sql += "values (nextval('acesso.seq_solicitacao'), '{}', '{}', '{}', '{}') returning id"
        sql = sql.format(self.solicitacao.get_email(), self.solicitacao.get_cnpj(), self.solicitacao.get_senha(), self.solicitacao.get_nome())

        cursor = self.conn.cursor()
        cursor.execute(sql)

        rs = cursor.fetchone()
        self.solicitacao.id = rs[0]
        self.conn.commit()
        cursor.close()

        return self.solicitacao;

    def confirmar_email(self, email):
        try:
            sql = "UPDATE acesso.solicitacoes set status = 2 where email = '{}'".format(email)
            
            cursor = self.conn.cursor()
            cursor.execute(sql)

            self.conn.commit()

        except Exception as ex:
            raise Exception(ex)            
        else:
            return dict({'status': "2"})   
        finally:
            cursor.close()

    def verificarSolicitacao(self):
        try:
            sql = " select s.id, s.email, s.cnpj, s.senha, s.nome"
            sql += " from acesso.solicitacoes s"
            sql += " where s.email = '{}'"
            sql = sql.format(self.solicitacao.get_email())

            cursor = self.conn.cursor()
            cursor.execute(sql)

            rs = cursor.fetchone()

            retorno = Solicitacao('','','','','')
            if rs != None:
                retorno = Solicitacao(rs[0], rs[1], rs[2], rs[3], rs[4])
        except Exception as ex:
            raise Exception(ex)
        else:
            return retorno

    def buscarSolicitacao(self, id):
        try:
            sql =  " select s.nome"
            sql += "       ,s.email"
            sql += "       ,s.senha"
            sql += "       ,e.id as id_empresa"
            sql += " from acesso.solicitacoes s"
            sql += " inner join acesso.empresas e on (e.cnpj = s.cnpj)"
            sql += " where s.id = '{}'"
            sql = sql.format(id)

            cursor = self.conn.cursor()
            cursor.execute(sql)

            rs = cursor.fetchone()

            usuario = []

            if rs != None:
                usuario = Usuario(rs[3], 0, rs[0], rs[1], rs[2])

        except Exception as ex:
            raise Exception(ex)
        else:
            return usuario


    def listar_confirmados(self, empresa):
        try:
            sql =  " select s.nome"
            sql += "        , s.email"
            sql += "        , s.senha"
            sql += "        , e.id as id_empresa"
            sql += "        , e.nome as nome_empresa"
            sql += "        , e.cnpj as cnpj"
            sql += "        , s.id"
            sql += "   from acesso.solicitacoes s"
            sql += "   join acesso.empresas e on e.cnpj = s.cnpj"
            sql += "  where s.status = 2 "
            sql += "    and e.cnpj = '{}' ".format(empresa.get_cnpj())

            cursor = self.conn.cursor()
            cursor.execute(sql)

            rs = cursor.fetchall()

        except Exception as ex:
            raise Exception(ex)
        else:
            return rs


    def aprovar_registro(self, usuario):
        try:
            sql = " INSERT INTO acesso.usuarios (id, nome, email, senha, empresa_id, data_criacao, status)"
            sql += " VALUES(nextval('acesso.seq_usuario'), '{}', '{}', '{}', '{}', '{}', 1) returning id"
            sql = sql.format(usuario.get_nome(), usuario.get_email(), usuario.get_senha(), usuario.get_empresa(), datetime.datetime.now())

            cursor = self.conn.cursor()
            cursor.execute(sql)
            rs = cursor.fetchone()
            id = rs[0]
            self.conn.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
        else:
            return id     

    def excluir_solicitacao(self, id):
        try:
            sql = "delete from acesso.solicitacoes where id = '{}'".format(id)

            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
        else:
            return "solicitação excluída."
