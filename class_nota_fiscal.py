class NotaFiscal:
    def __init__(self, pedido):
        self.codigo_pedido = pedido._codigo_pedido
        self.itens = pedido._itens_pedidos
        self.total = sum(item._preco_item for item in pedido._itens_pedidos)

    def gerar_nota(self):
        print("\n********** NOTA FISCAL **********")
        print(f"CÓDIGO DO PEDIDO: {self.codigo_pedido}")
        print("ITENS DO PEDIDO:")
        for i, item in enumerate(self.itens):
            print(f"  {i + 1}. Produto: {item._produto._descricao}")
            print(f"     Quantidade: {item._quantidade}")
            print(f"     Subtotal: R${item._preco_item:.2f}")
        print(f"\nTOTAL: R${self.total:.2f}")
        print("*********************************\n")
