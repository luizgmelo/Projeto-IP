from mesa import *

pedidos = []

def criar_pedido(id, num_mesa, produtos, preco, pagamento, data):
    return {
        "id": id, 
        "num_mesa": num_mesa,
        "produtos": produtos,
        "preco": preco,
        "pagamento": pagamento,
        "data": data
        }


def salvar_pedido(pedido):
    pedidos.append(pedido)
    return True


def pesquisar_pedido(mesa):
    if mesa:
        for pedido in pedidos:
            if (mesa["numero"] == pedido["num_mesa"]):
                return pedido
        return "Pedido não existe"
    else:
        return "Mesa não existe"


