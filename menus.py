def menu_principal():
    print("=" * 20)
    print(""" OPÇÕES DO SISTEMA:
            [1] - MESAS
            [2] - PEDIDOS
            [3] - PRODUTOS
            [4] - SAIR""")
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
   

def menu_pedido():
    print("=" * 20)
    print("""
            [1] - CADASTRAR PEDIDO
            [2] - LISTAR PEDIDOS
            [3] - EDITAR PEDIDO
            [4] - DELETAR PEDIDO
            [5] - VOLTAR""")
    print("=" * 20)

def menu_produtos():
    print("=" * 20)
    print("""
            [1] - CADASTRAR PRODUTO
            [2] - LISTAR PRODUTOS
            [3] - EDITAR PRODUTO
            [4] - DELETAR PRODUTO
            [5] - VOLTAR""")
    print("=" * 20)



