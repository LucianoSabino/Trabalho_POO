from class_funcionario import Funcionario
class Atendente(Funcionario):
    def __init__(self, nome, id):
        # Chama o construtor da classe pai (Funcionario)
        super().__init__(nome, id)
