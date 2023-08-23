funcionarios = []

def criar_funcionario(id, nome, salario, funcao):
    return {
        "id": id,
        "nome": nome,
        "salario": salario,
        "funcao":funcao
    }

def salvar_funcionario(funcionario):
    funcionarios.append(funcionario)
    return True

def pesquisar_funcionario(nome):
    for funcionario in funcionarios:
        if nome.lower() == funcionario["nome"].lower():
            return funcionario
        return "Funcionário não existe"
