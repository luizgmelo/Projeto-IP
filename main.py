from time import sleep
from mesa import *
from produtos import *
from funcionario import *
from menus import *




def main():
    ler_banco_mesa()
    ler_banco_produtos()
    ler_banco_funcionarios()
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
                num_mesa = str(input("Número da mesa: "))
                mesa_existe = verifica_mesa_existe(num_mesa)
                if mesa_existe:
                    editar_mesa(pesquisar_mesa(num_mesa))
                else:
                    print("Mesa não existe")
            elif opcao_mesa == '4':
                num_mesa = str(input("Número da mesa: "))
                mesa_existe = verifica_mesa_existe(num_mesa)
                if mesa_existe:
                    deletar_mesa(pesquisar_mesa(num_mesa))
                else:
                    print("Mesa não existe")
            elif opcao_mesa == '5':
                num_mesa = str(input("Número da mesa: "))
                mesa_existe = verifica_mesa_existe(num_mesa)
                if mesa_existe:
                    pesquisar_mesa(num_mesa)
                else:
                    print("Mesa não existe")
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
                nome_produto = str(input("Sabor da pizza que vai editar:"))
                produto_existe = verifica_produto_existe(nome_produto)
                if produto_existe:
                    editar_produto(pesquisar_produto(nome_produto))
                else:
                    print("Produto não existe")
            elif opcao_produto == '4':
                nome_produto = str(input("Digite o sabor da pizza que vai deletar: "))
                produto_existe = verifica_produto_existe(nome_produto)
                if produto_existe:
                    deletar_produto(pesquisar_produto(nome_produto))
                else:
                    print("Produto não existe")
            elif opcao_produto == '5':
                nome_produto = str(input("Digite o sabor da pizza que vai pesquisar: "))
                produto_existe = verifica_produto_existe(nome_produto)
                if produto_existe:
                    pesquisar_produto(nome_produto)
                else:
                    print("Produto não existe")
                
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
            elif opcao_funcionario == '6':
                print("Para pesquisar por data digite a data no seguinte formato (dia/mes/ano)")
                data_inicial = str(input("Data Inicial da pesquisa: ")) 
                data_final =  str(input("Data Final final da pesquisa: "))
                pesquisar_funcionario_por_data(data_inicial, data_final)

        if opcao == '4':
            salvar_banco_mesa()
            salvar_banco_produtos()
            salvar_banco_funcionarios()
            break
           

        
main()


