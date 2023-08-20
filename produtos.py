produtos = []

def criar_produto(id, nome, tamanho, preco,):
    return dict(id=id, nome=nome, tamanho=tamanho, preco=preco)

def salvar_produto(produto):
    produtos.append(produto)
    return True


