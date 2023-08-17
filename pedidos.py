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


def save_pedido(pedido):
    pedidos.append(pedido)
    return True 