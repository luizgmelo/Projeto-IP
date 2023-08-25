def menu_principal():
    print("=" * 20)
    print(""" OPÇÕES DO SISTEMA:
            [1] - MESAS
            [2] - PRODUTOS
            [3] - FUNCIONÁRIOS
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
            [5] - PESQUISAR MESA
            [6] - VOLTAR""")
    print("=" * 20)
    
    opcao = str(input("Opção: "))

    return opcao

def menu_produtos():
    print("=" * 20)
    print("""
            [1] - CADASTRAR PRODUTO
            [2] - LISTAR PRODUTOS
            [3] - EDITAR PRODUTO
            [4] - DELETAR PRODUTO
            [5] - PESQUISAR PRODUTO
            [6] - VOLTAR""")
    print("=" * 20)

    opcao = str(input("Opção: "))

    return opcao

def menu_funcionario():
    print('=' * 20)
    print("""
            [1] - CADASTRAR FUNCIONÁRIO
            [2] - LISTAR FUNCIONÁRIOS
            [3] - EDITAR FUNCIONÁRIO
            [4] - DELETAR FUNCIONÁRIO
            [5] - PESQUISAR FUNCIONÁRIO
            [6] - PESQUISAR FUNCIONARIO POR DATA DE CONTRATO
            [7] - VOLTAR""") 
    print('='*20)

    opcao = str(input("Opção: "))

    return opcao

def menu_editar_produto():
    print("=" * 20)
    print(""" 
         MENU EDITAR PRODUTO
         [1] - EDITAR NOME
         [2] - EDITAR TAMANHO
         [3] - EDITAR PREÇO
         [4] - EDITAR DESCRICAO
         [5] - VOLTAR""")
    print("=" * 20)
    
    opcao = str(input("Opção: "))

    return opcao

def menu_editar_funcionario():
    print("=" * 20)
    print(""" 
            MENU EDITAR FUNCIONARIO
            [1] - EDITAR NOME
            [2] - EDITAR SALARIO
            [3] - EDITAR FUNCAO DO FUNCIONARIO
            [4] - VOLTAR""")
    print("=" * 20)

    opcao = str(input("Opção: "))

    return opcao


