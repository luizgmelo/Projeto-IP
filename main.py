from time import sleep
from mesa import *
from pedidos import *
from produtos import *
from menus import *

banco_de_dados = {
    "mesas": mesas,
    "pedidos": pedidos,
    "produtos": produtos
    }



def main():
    id_produto = 0 
    while True:
        sleep(3)
        opcao = menu_principal()
        if opcao == '1':
            opcao_mesa = menu_mesas()
            if opcao_mesa == '1':
                num_mesa = str(input("Número da mesa: "))
                quant_cadeiras = int(input("Quantidade de cadeiras: "))
                salvar_mesa(criar_mesa(num_mesa, quant_cadeiras))
                print("Mesa cadastrada com sucesso!")
            elif opcao_mesa == '2':
                listar_mesas()
            elif opcao_mesa == '3':
                mesa = str(input("Número da mesa: "))
                editar_mesa(pesquisar_mesa(mesa))
            elif opcao_mesa == '4':
                mesa = str(input("Número da mesa: "))
                deletar_mesa(pesquisar_mesa(mesa))
        if opcao == '2':
            opcao_produto = menu_produtos()
            if opcao_produto == '1':
                id_produto += 1
                nome = str(input("Sabor da pizza: "))
                tamanho = str(input("Tamanho (P/M/G): "))
                preco = str(input("Preço: "))
                descricao = str(input("Descricao: "))
                salvar_produto(criar_produto(id_produto, nome, tamanho, preco, descricao))
                print("Produto cadastrado com sucesso!")
            elif opcao_produto == '2':
                listar_produtos()
            elif opcao_produto == '3':
                produto = str(input("Sabor da pizza que vai editar:"))
                print(editar_produto(produto))



main()


