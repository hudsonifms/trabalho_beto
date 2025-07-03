from util import *
from participantes import *
from eventos import *
from dados import *

def menu():
    user.append(menu)
    opcoes = [
        [menu_participantes, "Participantes"],
        [menu_eventos, "Eventos"],
        [None, "Encerrar e salvar"]
    ]
    
    mostrar_menu(opcoes, "---- [ Menu ] ----")
    input_menu(menu, opcoes, input("Escolha a Opção: "))

if __name__ == "__main__":
    limpar_terminal()
    print("---- SEJA BEM-VINDO ----")
    continuar("Pressione enter para continuar... ")
    limpar_terminal()
    menu()
    salvar_dados(temas, eventos, participantes) 