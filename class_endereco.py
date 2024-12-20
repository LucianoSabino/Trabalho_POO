# definição da classe
class Endereco:
    # definicão do construtor
    # em python podemos criar os atributos classe pelo construtor 
    def __init__(self, nome, cep, rua, numero, complemento, bairro, cidade, nome_entregador):
        self.__nome = nome
        self.__cep = cep # __ modificador de acesso private
        self.__rua = rua
        self.__numero = numero
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__nome_entregador = nome_entregador


    @property
    def _nome_entregador(self):
        return self.__nome_entregador

    @_nome_entregador.setter
    def _nome_entregador(self, value):
        self.__nome_entregador = value

    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value


    @property
    def _cep(self):
        return self.__cep

    @_cep.setter
    def _cep(self, value):
        self.__cep = value

    @property
    def _rua(self):
        return self.__rua

    @_rua.setter
    def _rua(self, value):
        self.__rua = value

    @property
    def _numero(self):
        return self.__numero

    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    @property
    def _complemento(self):
        return self.__complemento

    @_complemento.setter
    def _complemento(self, value):
        self.__complemento = value

    @property
    def _bairro(self):
        return self.__bairro

    @_bairro.setter
    def _bairro(self, value):
        self.__bairro = value

    @property
    def _cidade(self):
        return self.__cidade

    @_cidade.setter
    def _cidade(self, value):
        self.__cidade = value
