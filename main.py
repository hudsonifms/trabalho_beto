from util import *
from participantes import *


def menu():
 
    opcoes = [
        [menu_participantes, "Alunos"],
        [passar, "Eventos"],
        [passar, "Relatorios"],
        [passar, "Fechar"]
    ]
    
    mostrar_menu(opcoes, "---- [ Menu ] ----")
    tratar_input(menu, opcoes, int(input("Escolha a Opção: ")))
      
    
def passar():
        print("passar")
        
menu()

