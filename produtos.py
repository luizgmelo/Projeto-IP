from menus import menu_editar_produto
import json

produtos = []

def criar_produto(nome, tamanho, preco, descricao):
    return dict(nome=nome, tamanho=tamanho, preco=preco, descricao=descricao)

def salvar_produto(produto):
    produtos.append(produto)
    return True

def verifica_produto_existe(nome_produto):
    for produto in produtos:
        if nome_produto.lower() == produto["nome"].lower():
            return True 
    return False 

def pesquisar_produto(nome_produto):
    for produto in produtos:
        if nome_produto.lower() == produto["nome"].lower():
            print("="*30)
            print("Dados do produto {}".format(produto["nome"]).center(30))
            print("="*30)
            for chave, valor in produto.items():
                print("{}:".format(chave.capitalize()), valor)
            print("="*30)
            return produto 

def editar_produto(produto):
        # recebe o opcao do menu
        opcao = menu_editar_produto()
        # valida opcao
        if opcao not in '1234':
            return "Opcao nao existe"
        # funcao de cada opcao
        if opcao == '1':
            produto["nome"] = str(input("Digite o novo nome do produto: "))
            return print("Produto editado com sucesso")
        elif opcao == '2':
            produto["tamanho"] = str(input("Digite o novo tamanho do produto (P/M/G): ")).upper()
            return print("Produto editado com sucesso")
        elif opcao == '3':
            produto["preco"] = str(input("Digite o novo preço do produto: ")).replace(',', '.')
            return print("Produto editado com sucesso")
        elif opcao == '4':
            produto["descricao"] = str(input("Digite o novo preço do produto: ")).replace(',', '.')
            return print("Produto editado com sucesso")
        elif opcao == '5':
            # volta para o menu anterior
            return ''
        
def deletar_produto(produto):
    produtos.remove(produto)
    return print("Produto removido com sucesso!")

def listar_produtos():
    if produtos == []:
        print("Não existe produto cadastrado no sistema")
    else:
        print("="*30)
        print("Listagem dos produtos".center(30))
        print("="*30)
        # pega os dicionarios da lista
        for produto in produtos:
            for chave, valor in produto.items():
                print("{}:".format(chave.capitalize()), valor)
            print("-"*30)
        print("="*30)


def salvar_banco_produtos():
    with open('banco_produtos.json', 'w') as banco_produtos:
        json.dump(produtos, banco_produtos, indent=4)

def ler_banco_produtos():
    with open('banco_produtos.json', 'r') as banco_produtos:
        global produtos
        produtos = json.load(banco_produtos)
