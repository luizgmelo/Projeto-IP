from menus import *

def main():
    while True:
        opcao_escolhida = menu_principal()

        if opcao_escolhida not in '123':
            print("\nOpção Inválida. Tente Novamente\n")
            continue

        if opcao_escolhida == '1':
            print("MENU Opções de Cadastros")
        elif opcao_escolhida == '2':
            print("MENU Opções de Consultas")
        elif opcao_escolhida == '3':
            break


main()
print("Programa Finalizado com Sucesso. Até mais.")


