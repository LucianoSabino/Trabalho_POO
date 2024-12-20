from class_nota_fiscal import NotaFiscal  

class Pedido:
    # Definição do construtor original com endereço e id_garcom
    def __init__(self, codigo_pedido, endereco_entrega=None, numero_mesa=None, id_garcom=None):
        self.__codigo_pedido = codigo_pedido
        self.__endereco_entrega = endereco_entrega  # Pode ser None se número da mesa for fornecido
        self.__numero_mesa = numero_mesa  # Número da mesa, caso fornecido
        self.__status = 0  # 0 = aberto, 1 = finalizado/pago
        self.__id_garcom = id_garcom  # Novo atributo id_garcom, inicializado como None
        # Criando uma estrutura para armazenar itens do pedido
        self.__itens_pedidos = []

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        # Se o pedido for finalizado, gere a nota fiscal
        if value == 1:  # Status 1 significa pedido finalizado
            nota_fiscal = NotaFiscal(self)  # Cria uma NotaFiscal
            nota_fiscal.gerar_nota()  # Chama o método para imprimir a nota fiscal
            self.__status = value

    @property
    def _codigo_pedido(self):
        return self.__codigo_pedido

    @_codigo_pedido.setter
    def _codigo_pedido(self, value):
        self.__codigo_pedido = value

    @property
    def _endereco_entrega(self):
        return self.__endereco_entrega

    @_endereco_entrega.setter
    def _endereco_entrega(self, value):
        self.__endereco_entrega = value

    @property
    def _numero_mesa(self):
        return self.__numero_mesa

    @_numero_mesa.setter
    def _numero_mesa(self, value):
        self.__numero_mesa = value

    @property
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value

    # Adicionando o getter e setter para o atributo id_garcom
    @property
    def id_garcom(self):
        return self.__id_garcom

    @id_garcom.setter
    def id_garcom(self, value):
        self.__id_garcom = value

    def adicionar_item_ao_pedido(self, itempedido):
        self.__itens_pedidos.append(itempedido)

    def remover_item_pedido(self, codigo_item):
        self.__itens_pedidos.pop(codigo_item)

    def quantidade_itens_pedido(self):
        return int(len(self.__itens_pedidos))

    def toString(self):
        str_line = "** INÍCIO DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')
        str_line = "CÓDIGO DO PEDIDO:" + str(self._codigo_pedido)
        print(str_line, end='\t')
        str_line = "STATUS DO PEDIDO:" + str(self.status)  # (0-aberto | 1-finalizado)
        print(str_line, end='\n')
        
        if self._endereco_entrega:  # Se houver endereço
            str_line = "CEP ENDEREÇO PARA ENTREGA:" + str(self._endereco_entrega._cep)
            print(str_line, end='\t')
            str_line = "RUA:" + str(self._endereco_entrega._rua)
            print(str_line, end='\t')
            str_line = "BAIRRO/CIDADE PARA ENTREGA:" + str(self._endereco_entrega._bairro) + "/" + str(self._endereco_entrega._cidade)
            print(str_line, end='\n')
        else:  # Caso tenha número de mesa
            str_line = "NÚMERO DA MESA:" + str(self._numero_mesa)
            print(str_line, end='\n')
            str_line = "ID DO GARÇOM:" + str(self.id_garcom)
            print(str_line, end='\n')

        str_line = "QUANTIDADE DE ITENS DO PEDIDO:" + str(self.quantidade_itens_pedido())
        print(str_line, end='\n')
        dbl_preco_total = 0.0
        for i, item in enumerate(self._itens_pedidos):
            str_line = "\t #ITEM:" + str(i)
            print(str_line, end='\t')
            str_line = "PRODUTO:" + str(item._produto._descricao)
            print(str_line, end='\t')
            str_line = "QTD (#):" + str(item._quantidade)
            print(str_line, end='\t')
            str_line = "SUBTOTAL (R$):" + str(item._preco_item)
            dbl_preco_total += item._preco_item
            print(str_line, end='\n')
        str_line = "PREÇO TOTAL DO PEDIDO:" + str(dbl_preco_total)
        print(str_line, end='\n')
        str_line = "** FIM DAS INFORMAÇÕES DO PEDIDO **"
        print(str_line, end='\n')