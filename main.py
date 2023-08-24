from time import sleep
from mesa import *
from pedidos import *
from produtos import *
from funcionario import *
from menus import *




def main():
    ler_banco_mesa()
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
                nome = str(input("Sabor da pizza: "))
                tamanho = str(input("Tamanho (P/M/G): "))
                preco = str(input("Preço: "))
                descricao = str(input("Descricao: "))
                salvar_produto(criar_produto(nome, tamanho, preco, descricao))
                print("Produto cadastrado com sucesso!")
            elif opcao_produto == '2':
                listar_produtos()
            elif opcao_produto == '3':
                produto = str(input("Sabor da pizza que vai editar:"))
                print(editar_produto(produto))
            elif opcao_produto == '4':
                produto = str(input("Digite o sabor da pizza que vai deletar: "))
                print(deletar_produto(produto))
        if opcao == '3':
            opcao_funcionario = menu_funcionario()
            if opcao_funcionario == '1':
                nome = str(input("Digite o nome do funcionário: "))
                salario = str(input("Digite o salário do funcionário: "))
                funcao = str(input("Digite a função do funcionário: "))
                (salvar_funcionario(criar_funcionario(nome, salario, funcao)))
                print("Funcionário cadastrado com sucesso!")
            elif opcao_funcionario == '2':
                listar_funcionario()
            elif opcao_funcionario == '3':
                nome_funcionario = str(input("Digite o nome do funcionário: "))
                funcionario_existe = verifica_funcionario_existe(nome_funcionario)
                if funcionario_existe:
                    editar_funcionario(pesquisar_funcionario(nome_funcionario))
                else:
                    print("Funcionário não existe")
            elif opcao_funcionario == '4':
                nome_funcionario = str(input("Digite o nome do funcionário que vai deletar: "))
                funcionario_existe = verifica_funcionario_existe(nome_funcionario)
                if funcionario_existe:
                    deletar_funcionario(pesquisar_funcionario(nome_funcionario))
                else:
                    print("Funcionário não existe")
            elif opcao_funcionario == '5':
                nome_funcionario = str(input("Digite o nome do funcionário que vai pesquisar: "))
                funcionario_existe = verifica_funcionario_existe(nome_funcionario)
                if funcionario_existe:
                    pesquisar_funcionario(nome_funcionario)
                else:
                    print("Funcionário não existe")              
        if opcao == '4':
            salvar_banco_mesa()
            break
           

        
main()


