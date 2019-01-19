class Usuario(object):
    def __init__(self, empresa, id, nome, email, senha):
        self.empresa = empresa
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    def get_id(self):
        return self.id

    def get_empresa(self):
        return self.empresa

    def get_nome(self):
        return self.nome

    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha
