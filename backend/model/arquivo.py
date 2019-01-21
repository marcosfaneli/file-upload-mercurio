import hashlib
from common.config import URL_FILES, KEY


class Arquivo(object):
    def __init__(self, descricao, categoria, keys, tipo, data_postado, usuario_postou, arquivo, tamanho, id):
        self.descricao = descricao
        self.categoria = categoria
        self.keys = keys
        self.tipo = tipo
        self.id = id
        self.data_postado = data_postado
        self.usuario_postou = usuario_postou
        self.classificacao = 1
        self.arquivo = arquivo
        self.tamanho = tamanho

    def get_descricao(self):
        return self.descricao

    def get_categoria(self):
        return self.categoria

    def get_keys(self):
        return self.keys

    def get_tipo(self):
        return self.tipo

    def get_id(self):
        return self.id

    def get_classificacao(self):
        return self.classificacao

    def get_usuario_postou(self):
        return self.usuario_postou

    def get_data_postado(self):
        return self.data_postado

    def get_arquivo(self):
        return self.arquivo

    def get_tamanho(self):
        return self.tamanho

    def get_hash(self):
        str = '{}|{}|{}|{}|{}|{}'.format(KEY, self.descricao, self.categoria.get_id(), self.usuario_postou.get_id(), self.usuario_postou.get_empresa().get_id(), self.tipo)

        b = bytes(str, 'utf-8')
        hash_object = hashlib.sha256(b)
        hex = hash_object.hexdigest()
        value = '{}'.format(hex)

        return value


    def get_url(self):
        return '{}/download/{}'.format(URL_FILES, self.get_hash())
