class Categoria(object):
    def __init__(self, id, nome, cor):
        self.id = id
        self.nome = nome
        self.cor = cor

    def get_nome(self):
        return self.nome

    def get_id(self):
        return self.id

    def get_cor(self):
        return self.cor
