from common.conexao import get_conexao
from model.solicitacao import Solicitacao

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
        self.conn.commit();
        cursor.close;

        return self.solicitacao;

    def aceitarSolicitacao(self):
        pass

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