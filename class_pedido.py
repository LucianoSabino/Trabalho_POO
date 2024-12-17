from class_nota_fiscal import NotaFiscal  

class Pedido:
    # definição do construtor
    def __init__(self, codigo_pedido, endereco_entrega):
        self.__codigo_pedido = codigo_pedido
        self.__endereco_entrega = endereco_entrega
        self.__status = 0  # 0 = aberto, 1 = finalizado/pago
        # criando uma estrutura para armazenar itens do pedido
        self.__itens_pedidos = []

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        # Se o pedido for finalizado , gere a nota fiscal
        if value == 1:  # Status 1 significa pedido finalizado
            nota_fiscal = NotaFiscal(self)  # Cria uma  NotaFiscal
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
    def _itens_pedidos(self):
        return self.__itens_pedidos

    @_itens_pedidos.setter
    def _itens_pedidos(self, value):
        self.__itens_pedidos = value

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
        str_line = "CEP ENDEREÇO PARA ENTREGA:" + str(self._endereco_entrega._cep)
        print(str_line, end='\t')
        str_line = "RUA:" + str(self._endereco_entrega._rua)
        print(str_line, end='\t')
        str_line = "BAIRRO/CIDADE PARA ENTREGA:" + str(self._endereco_entrega._bairro) + "/" + str(self._endereco_entrega._cidade)
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
