class Empresa(object):

    def __init__(self, cnpj, nome, id, alias):
        self.cnpj = cnpj
        self.nome = nome
        self.id = id
        self.alias = alias

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_cnpj(self):
        return self.cnpj

    def get_alias(self):
        return self.alias

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj

    def set_alias(self, alias):
        self.cnpj = alias
