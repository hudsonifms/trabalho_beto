from util import *
from participantes import *
from eventos import *
import json

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

def dados(nome_arquivo, variavel, tipo):
    if tipo == "w":
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(variavel, arquivo, ensure_ascii=False, indent=4)
    elif tipo == "r":
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return None
        
dados("eventos.json", eventos, "r")
dados("temas.json", temas, "r")
dados("participantes.json", participantes, "r")
menu()
dados("eventos.json", eventos, "w")
dados("temas.json", temas, "w")
dados("participantes.json", participantes, "w")

