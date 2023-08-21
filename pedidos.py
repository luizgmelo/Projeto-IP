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

def salvar_pedido(pedido, mesa_existe):
    if mesa_existe:
        pedidos.append(pedido)
        return "Pedido criado com sucesso!"
    else:
        return "Mesa não existe.\nÉ criar uma mesa para fazer o pedido."


def pesquisar_pedido(mesa):
    if mesa:
        for pedido in pedidos:
            if (mesa["numero"] == pedido["num_mesa"]):
                return pedido
        return "Pedido não existe"
    else:
        return "Mesa não existe"


def deletar_pedido(num_mesa):
    for pedido in pedidos:
        if (num_mesa == pedido["num_mesa"]):
            pedidos.remove(pedido)
            return "Pedido removido com sucesso!" 
    return "Pedido não existe"
    

def listar_pedidos():
    if pedidos == []:
        return print("Não há pedidos")
    else:
        print("="*30)
        print("Listagem dos pedidos".center(30))
        print("="*30)
        for pedido in pedidos:
            for chave,valor in pedido.items():
                print("{}:".format(chave.capitalize()), valor)
            print("-"*30)
    print("="*30)


