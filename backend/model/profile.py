class Profile(object):
    def __init__(self, usuario, quantidade, tamanho):
        self.usuario = usuario
        self.quantidade = quantidade
        self.tamanho = tamanho

    def get_usuario(self):
        return self.usuario

    def get_quantidade(self):
        return self.quantidade

    def get_tamanho(self):
        return self.tamanho
