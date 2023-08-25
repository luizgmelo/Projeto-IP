from menus import menu_editar_funcionario
import json
from datetime import datetime

funcionarios = []
data_hoje = datetime.today()

def criar_funcionario(nome, salario, funcao):
    return {"nome": nome.capitalize(),"salario": salario,"funcao": funcao, "data_contrato": data_hoje.strftime('%d/%m/%Y')}

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

def pesquisar_funcionario_por_data(data_inicial, data_final):
    data_inicial_formato_data = datetime.strptime(data_inicial, '%d/%m/%Y').date()
    data_final_formato_data = datetime.strptime(data_final, '%d/%m/%Y').date()
    if funcionarios == []:
        print("Não há funcionario cadastrado")
    for funcionario in funcionarios:
        data_contrato_formato_data = datetime.strptime(funcionario["data_contrato"], '%d/%m/%Y').date()
        if data_inicial_formato_data <= data_contrato_formato_data <= data_final_formato_data:
            print("="*30)
            print("Nome do Funcionário:",funcionario["nome"])
            print("Salário:",funcionario["salario"])
            print("Função:",funcionario["funcao"])
            print("Data de Contrato:",funcionario["data_contrato"])
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
            print("Data de Contrato:",funcionario["data_contrato"])
            print("="*30)
        print("="*30)

def salvar_banco_funcionarios():
    with open("banco_funcionarios.json", "w") as banco_funcionario:
        json.dump(funcionarios, banco_funcionario, indent=4)

def ler_banco_funcionarios():
    with open("banco_funcionarios.json", "r") as banco_funcionario:
        global funcionarios
        funcionarios = json.load(banco_funcionario)


