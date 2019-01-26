class Profile(object):
    def __init__(self, usuario, quantidade, tamanho, solicitacoes):
        self.usuario = usuario
        self.quantidade = quantidade
        self.tamanho = tamanho
        self.solicitacoes = solicitacoes

    def get_usuario(self):
        return self.usuario

    def get_quantidade(self):
        return self.quantidade

    def get_tamanho(self):
        return self.tamanho

    def get_solicitacoes(self):
        return self.solicitacoes
