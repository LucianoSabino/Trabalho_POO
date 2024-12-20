from class_endereco import Endereco
from class_item_pedido import ItemPedido
from class_pedido import Pedido
from class_produto import Produto
from class_nota_fiscal import NotaFiscal
from class_funcionario import Funcionario
from class_antendete import Atendente
from class_garçom import Garcom
from datetime import datetime
from incializador import garcons
def menu_principal():  # MENU PRINCIPAL
    print('''
        MENU Principal:
        [1] - Controle de vendas
        [2] - Cadastrar novo produto
        [3] - Remover um produto
        [4] - Pesquisar um produto
        [5] - Cadastrar novo funcionario
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def Cadastrar_novo_funcionario():
    opcao_escolhida = int(input("[1] - garçon\n[2] - atendente\n5"))
    if(opcao_escolhida == 1):
       garcons.append(criar_garcom())
    if(opcao_escolhida == 2):
        atendente.append(criar_garcom())

# Função para criar um Garçom
def criar_garcom():
    nome = input("Digite o nome do garçom: ")
    id = int(input("Digite o ID do garçom: "))
    n_mesa = input("Digite os números das mesas que pode ser atendida (separados por vírgula): ")
    n_mesa = [int(x) for x in n_mesa.split(',')]  # Convertendo para lista de números inteiros
    return Garcom(nome, id, n_mesa)

# Função para criar um Atendente
def criar_atendente():
    nome = input("Digite o nome do atendente: ")
    id = int(input("Digite o ID do atendente: "))
    return Atendente(nome, id)

def menu_pedido():
    print('''
        MENU Vendas:
        [1] - Abrir novo pedido
        [2] - Adicionar item ao pedido
        [3] - Remover item do pedido
        [4] - Listar itens do pedido em detalhes
        [5] - Finalizar pedido e imprimir
        [s] - Sair
    ''')
    return str(input('Escolha uma opção: '))

def buscar_garcom_para_mesa(numero_mesa):
    for i in range(len(garcons)):
        # Verifica se n_mesa é uma lista e se contém o numero_mesa
        if isinstance(garcons[i].n_mesa, list):
            for j in range(len(garcons[i].n_mesa)):
                if (garcons[i].n_mesa[j] == numero_mesa):
                    print(garcons[i].id)
                    return garcons[i].id
        # Caso n_mesa seja um único número, verificamos diretamente
        elif garcons[i].n_mesa == numero_mesa:
            return garcons[i].id

    return None  # Caso não encontre nenhum garçom para a mesa


def pedido_adicionar():
    opcao_escolhida = int(input("[1] - Mesa [2] - Delivery: "))
    
    if opcao_escolhida == 2:  # Delivery
        endereco = cadastrar_endereco()  # Cadastra o endereço
        codigo_pedido = len(pedidos) + 1  # Gera o código do pedido
        pedido = Pedido(codigo_pedido, endereco_entrega=endereco)  # Cria um pedido de entrega
        return pedido
    
    elif opcao_escolhida == 1:  # Mesa
        numero_mesa = int(input("Digite o número da mesa: "))
        id = buscar_garcom_para_mesa(numero_mesa)
        print(id)
        codigo_pedido = len(pedidos) + 1  # Gera o código do pedido
        pedido = Pedido(codigo_pedido, numero_mesa=numero_mesa, id_garcom=id)  # Cria um pedido de mesa
        return pedido


def pedido_adicionar_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para adicionar um novo item: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_produto = int(input('Informe o código do produto para adicionar ao pedido: '))
        produto = buscar_produto_por_codigo(int_codigo_produto)
        if produto:
            int_quantidade_item = int(input('Informe a quantidade do item:'))
            novo_item_pedido = ItemPedido(produto, int_quantidade_item)
            pedido.adicionar_item_ao_pedido(novo_item_pedido)
        else:
            print("Não foi possível adicionar este produto, pois o código do produto não existe!")
        #return Pedido(codido_pedido, endereco_pedido)
    else:
        print("Pedido inexistente")
        return False
    
def pedido_remover_item():
    int_pedido_selecionado = int(input('Informe o código do pedido para remover um item selecionado: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        int_codigo_item = int(input('Informe o número do item para remover deste pedido ' + str(pedido._codigo_pedido) + ': '))
        # verifica se número intem informado existe: não faz sentido remover item 5 se ele não existe
        #if pedido.quantidade_itens_pedido() <= int_codigo_item:
        pedido.remover_item_pedido(int_codigo_item)
    else:
        print("Pedido inexistente")
        return False
    
def pedido_listar_items():
    int_pedido_selecionado = int(input('Informe o código do pedido para mais detalhes: '))
    if buscar_pedido_por_codigo(int_pedido_selecionado):
        # verificar se pedido existe
        pedido = pedidos[int_pedido_selecionado]
        pedido.toString()
    else:
        print("Pedido inexistente")
        return False
    
def cadastrar_endereco():
    str_cep = str(input('Informe o cep do endereço: '))
    str_rua = str(input('Informe a rua: '))
    int_num = int(input('Informe o número: '))
    str_complemento = str(input('Informe o complemento do endereço: '))
    str_bairro = str(input('Informe o bairro: '))
    str_cidade = str(input('Informe a cidade: '))
    endereco = Endereco(str_cep, str_rua, int_num,
                        str_complemento, str_bairro, str_cidade)
    return endereco

def cadastrar_produto():
    int_codigo = int(input('Informe o código identificador do produto: '))
    str_nome = str(input('Qual o nome/descrição do produto? '))
    flt_preco = float(input('Informe o valor (ex. 0.00): '))
    date_validade = (input('Informe a validade do produto (formato dd/mm/aaaa): '))
    date_validade = datetime.strptime(date_validade, '%d/%m/%Y')
    return Produto(int_codigo, str_nome, flt_preco, date_validade)

def remover_produto():
    int_codigo_remocao = int(input('Informe o código do produto para remoção: '))
    produto_remover = estoque_produtos[int_codigo_remocao]
    print("Produto (" + produto_remover._descricao + ") removido!") 
    del estoque_produtos[int_codigo_remocao]

def buscar_produto_por_codigo(int_codigo_produto):
    # Verifica se existe produto cadastrado
    for chave in estoque_produtos.keys():
        if chave == int_codigo_produto:
            return estoque_produtos[int_codigo_produto]
    return False

def buscar_pedido_por_codigo(int_codigo_pedido):
    # Verifica se existe produto cadastrado
    for chave in pedidos.keys():
        if chave == int_codigo_pedido:
            return pedidos[int_codigo_pedido]
    return False

# Aplicação de exemplo disciplina POO - UFRB
# Sistema de controle de pedidos
# Professor Guilherme Braga Araújo

estoque_produtos = {}
pedidos = {}
atendente = []
while True:
    # menu_principal
    opcao_escolhida = menu_principal()
    # verificando escolha
    # opc sair
    if (opcao_escolhida == "s"):
        break
    # opc 1
    elif (opcao_escolhida == "1"):
        while True:
            opcao_escolhida = menu_pedido()
            # opc menu vendas - novo pedido
            if (opcao_escolhida == "1"):
                pedido = pedido_adicionar()
                if (pedido):
                    # adiciona pedido ao sistema
                    pedidos[pedido._codigo_pedido] = pedido
            # opc menu vendas - adicionar item    
            elif (opcao_escolhida == "2"):
                pedido_adicionar_item()
            elif (opcao_escolhida == "3"):
                pedido_remover_item()
            elif (opcao_escolhida == "4"):
                pedido_listar_items()
            elif (opcao_escolhida == "5"):
                pedido.status = 1
            else:
                # Volta para o menu principal
                break
               
    # opc 2
    elif (opcao_escolhida == "2"):
        produto = cadastrar_produto()
        if (produto):
            # adiciona produto ao nosso estoque
            estoque_produtos[produto._codigo_produto] = produto
    # opc 3
    elif (opcao_escolhida == "3"):
        remover_produto()
    # opc 4
    elif (opcao_escolhida == "4"):
        int_codigo_produto = int(input('Informe o código do produto para busca: '))
        produto_pesquisa = buscar_produto_por_codigo(int_codigo_produto)
        if (produto_pesquisa):
            print("Produto encontrado:")
            print(">Código=" + str(produto_pesquisa._codigo_produto))
            print(">Descricao=" + produto_pesquisa._descricao)
            print(">Valor=" + str(produto_pesquisa._preco))
            print(">Validade=" + str(produto_pesquisa._validade))
        else:
            print("Produto nâo cadastrado/encontrado.")
    elif (opcao_escolhida == "5"):
        Cadastrar_novo_funcionario()
    else:
        print("A opção escolhida é inválida.")
