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


