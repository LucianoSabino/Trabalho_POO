class Funcionario:
    def __init__(self, nome, id):
        self.__nome = nome  # Atributo privado
        self.__id = id      # Atributo privado

    # Getter para 'nome'
    @property
    def nome(self):
        return self.__nome

    # Setter para 'nome'
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # Getter para 'id'
    @property
    def id(self):
        return self.__id

    # Setter para 'id'
    @id.setter
    def id(self, id):
        self.__id = id