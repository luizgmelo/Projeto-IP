mesas = []

def criar_mesa(numero, quant_cadeiras):
    return {"numero": numero, "quant_cadeiras": quant_cadeiras}

def salvar_mesa(mesa):
    mesas.append(mesa)
    return True

def pesquisar_mesa(numero):
    for mesa in mesas:
        if numero == mesa["numero"]:
            return mesa
    return False

def editar_mesa(mesa):
    if mesa:
        mesa["quant_cadeiras"] = int(input("Digite a nova quantidade de cadeiras: "))
        return True
    else:
        return print("Mesa não existe")

def deletar_mesa(mesa):
    if mesa:
        mesas.remove(mesa)
        return True
    else:
        return print("Mesa não existe")

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


