from class_funcionario import Funcionario
class Garcom(Funcionario):
    def __init__(self, nome, id, n_mesa):
        # Chama o construtor da classe pai (Funcionario)
        super().__init__(nome, id)
        self.__n_mesa = n_mesa  # Atributo privado

    # Getter para 'n_mesa'
    @property
    def n_mesa(self):
        return self.__n_mesa

    # Setter para 'n_mesa'
    @n_mesa.setter
    def n_mesa(self, n_mesa):
        self.__n_mesa = n_mesa
