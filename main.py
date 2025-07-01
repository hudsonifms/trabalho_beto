from util import *
from participantes import *
from eventos import *

def menu():
    user.append(menu)
    opcoes = [
        [menu_participantes, "Alunos"],
        [menu_eventos, "Eventos"],
        [None, "Relatorios"],
        [None, "Fechar"]
    ]
    
    
    mostrar_menu(opcoes, "---- [ Menu ] ----")
    input_menu(menu, opcoes, input("Escolha a Opção: "))
      
menu()


