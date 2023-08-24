import json

mesas = []

def criar_mesa(numero, quant_cadeiras):
    return {"numero": numero, "quant_cadeiras": quant_cadeiras}

def salvar_mesa(mesa):
    mesas.append(mesa)
    return True

def verifica_mesa_existe(numero):
    for mesa in mesas:
        if numero == mesa["numero"]:
            return True 
    return False

def pesquisar_mesa(numero):
    for mesa in mesas:
        if numero == mesa["numero"]:
            print("="*30)
            print("Dados da mesa {}".format(numero).center(30))
            print("="*30)
            print("Mesa", mesa["numero"])
            print("Quantidade de Cadeiras:", mesa["quant_cadeiras"])
            print("="*30)
            return mesa

def editar_mesa(mesa):
    mesa["quant_cadeiras"] = int(input("Digite a nova quantidade de cadeiras: "))
    return print("Mesa editada com sucesso")

def deletar_mesa(mesa):
    mesas.remove(mesa)
    return print("Mesa deletada com sucesso")

def listar_mesas():
    if mesas == []:
        return print("Não há mesas")
    else:
        print("="*30)
        print("Listagem das mesas".center(30))
        print("="*30)
        for mesa in mesas:
            print("Mesa", mesa["numero"])
            print("Quantidade de Cadeiras:", mesa["quant_cadeiras"])
            print("-"*30)
        print("="*30)

def ler_banco_mesa():
    with open('banco_mesa.json', 'r') as banco_mesa:
        global mesas
        mesas = json.load(banco_mesa)

def salvar_banco_mesa():
    with open('banco_mesa.json', 'w') as banco_mesa:
        json.dump(mesas, banco_mesa, indent=4)
