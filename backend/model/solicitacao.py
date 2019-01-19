class Solicitacao(object):
    def __init__(self, id, email, cnpj, senha, nome):
        self.id = id
        self.email = email
        self.cnpj = cnpj
        self.senha = senha
        self.nome = nome

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def get_cnpj(self):
        return self.cnpj

    def get_senha(self):
        return self.senha

    def get_nome(self):
        return self.nome
    