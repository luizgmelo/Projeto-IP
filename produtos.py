from menus import menu_editar_produto

produtos = []

def criar_produto(id, nome, tamanho, preco,):
    return dict(id=id, nome=nome, tamanho=tamanho, preco=preco)

def salvar_produto(produto):
    produtos.append(produto)
    return True

def pesquisar_produto(nome_produto):
    for produto in produtos:
        if nome_produto.lower() == produto["nome"].lower():
            return produto 
    else:
        return "Produto não existe.\nVerifique se há erros de digitação.\nDigite o nome do produto completo para a pesquisa ter sucesso."

def editar_produto(nome_produto):
    # busca o produto
    for produto in produtos:
        if nome_produto.lower() == produto["nome"].lower():
            # recebe o opcao do menu
            opcao = menu_editar_produto()
            # valida opcao
            if opcao not in '1234':
                return "Opcao nao existe"
            # funcao de cada opcao
            if opcao == '1':
                produto["nome"] = str(input("Digite o novo nome do produto: "))
                return "Produto editado com suceso"
            elif opcao == '2':
                produto["tamanho"] = str(input("Digite o novo tamanho do produto (P/M/G): ")).upper()
                return "Produto editado com suceso"
            elif opcao == '3':
                produto["preco"] = str(input("Digite o novo preço do produto: ")).replace(',', '.')
                return "Produto editado com suceso"
            elif opcao == '4':
                # volta para o menu anterior
                return ''
    return "Produto não existe.\nVerifique se há erros de digitação.\nDigite o nome do produto completo para a edicao ter sucesso."
        
