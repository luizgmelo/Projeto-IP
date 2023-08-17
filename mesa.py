mesas = []

def criar_mesa(numero, quant_cadeiras):
    return {"numero": numero, "quant_cadeiras": quant_cadeiras}

def save_mesa(mesa):
    mesas.append(mesa)
    return True
