def menu_principal():
    print("=" * 20)
    print(""" OPÇÕES DO SISTEMA:
            [1] - MESAS
            [2] - PRODUTOS
            [3] - SAIR""")
    print("=" * 20)
    opcao = str(input("Opção: "))
    return opcao

def menu_mesas():
    print("=" * 20)
    print("""
            [1] - CADASTRAR MESA
            [2] - LISTAR MESAS
            [3] - EDITAR MESA
            [4] - DELETAR MESA
            [5] - VOLTAR""")
    print("=" * 20)
    
    opcao = str(input("Opcão: "))

    return opcao

def menu_pedido():
    print("=" * 20)
    print("""
            [1] - CADASTRAR PEDIDO
            [2] - LISTAR PEDIDOS
            [3] - EDITAR PEDIDO
            [4] - DELETAR PEDIDO
            [5] - VOLTAR""")
    print("=" * 20)

    opcao = str(input("Opcão: "))

    return opcao

def menu_produtos():
    print("=" * 20)
    print("""
            [1] - CADASTRAR PRODUTO
            [2] - LISTAR PRODUTOS
            [3] - EDITAR PRODUTO
            [4] - DELETAR PRODUTO
            [5] - VOLTAR""")
    print("=" * 20)

    opcao = str(input("Opcão: "))

    return opcao

def menu_editar_produto():
    print("=" * 20)
    print(f""" MENU EDITAR PRODUTO
[1] - EDITAR NOME
[2] - EDITAR TAMANHO
[3] - EDITAR PRECO
[4] - VOLTAR""")
    print("=" * 20)
    
    escolha = str(input("Escolha: "))

    return escolha





