from util import *
from participantes import *


def menu():
    user.append(menu)
    opcoes = [
        [menu_participantes, "Alunos"],
        [passar, "Eventos"],
        [passar, "Relatorios"],
        [None, "Fechar"]
    ]
    
    mostrar_menu(opcoes, "---- [ Menu ] ----")
    tratar_input(menu, opcoes, int(input("Escolha a Opção: ")))
      
    
def passar():
        print("passar")
        
while True:
    menu()

