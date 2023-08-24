from menus import menu_editar_funcionario

funcionarios = []

def criar_funcionario(nome, salario, funcao):
    return {"nome": nome.capitalize(),"salario": salario,"funcao": funcao}

def salvar_funcionario(funcionario):
    funcionarios.append(funcionario)
    return True

def verifica_funcionario_existe(nome):
    for funcionario in funcionarios:
        if nome.lower() == funcionario["nome"].lower():
            return True
    return False

def pesquisar_funcionario(nome):
    print ("="*30)
    print("Dados do funcionário {}".format(nome.capitalize()).center(30))
    print("="*30)
    for funcionario in funcionarios:
        if nome.lower() == funcionario["nome"].lower():
            print("Nome do Funcionário:",funcionario["nome"])
            print("Salário:",funcionario["salario"])
            print("Função:",funcionario["funcao"])
            return funcionario
    print("="*30)
    
def editar_funcionario(funcionario):
    opcao = menu_editar_funcionario()
    if opcao == '1':
        funcionario["nome"] = str(input("Digite o novo nome do funcionário: ")).capitalize()
        return print("Funcionário editado com sucesso")
    elif opcao == '2':
        funcionario["salario"] = str(input("Digite o novo salário do funcionário: "))
        return print("Funcionário editado com sucesso")
    elif opcao == '3':
        funcionario["funcao"] = str(input("Digite a nova função do funcionário: "))
        return print("Funcionário editado com sucesso")
    elif opcao == '4':
        return ''
    else:
        print("Opção inválida!")

def deletar_funcionario(funcionario):
    funcionarios.remove(funcionario)
    return print ("Funcionário deletado com sucesso! ")
    
def listar_funcionario():
    if funcionarios == []:
        return print("Não há fucionários")
    else:
        print ("="*30)
        print("Listagem dos funcionários".center(30))
        print("="*30)
        for funcionario in funcionarios:
            print("Nome do Funcionário:",funcionario["nome"])
            print("Salário:",funcionario["salario"])
            print("Função:",funcionario["funcao"])
            print("="*30)
        print("="*30)
