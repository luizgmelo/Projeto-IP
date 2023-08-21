produtos = []

def criar_produto(id, nome, tamanho, preco,):
    return dict(id=id, nome=nome, tamanho=tamanho, preco=preco)

def salvar_produto(produto):
    produtos.append(produto)
    return True

def pesquisar_produto(nome):
    for produto in produtos:
        if nome.lower() == produto["nome"].lower():
            return produto 
    else:
        return "Produto não existe.\nVerifique se há erros de digitação.\nDigite o nome do produto completo para a pesquisa ter sucesso."

