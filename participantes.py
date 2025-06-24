from util import *
 
participantes = {}

'''
{
    nome:
    cpf:
    idade:
    email: 
    temas_preferidos:
}
'''
def menu_participantes():
    opcoes = [
        [cadastrar_participante, "Cadastrar participante"],
        [buscar_participante, "Buscar Participante"],
        [cadastrar_participante, "Cadastrar participantes"],
        [cadastrar_participante, "Cadastrar participantes"]
    ]

    mostrar_menu(opcoes, "---- [ PARTICIPANTES ] ----")
    tratar_input(menu_participantes, opcoes, int(input("Escolha a Opção: ")))


def cadastrar_participante():   
    dados = form("Nome", "Cpf", "Idade", "Email", "Telefone")
    participantes[dados["cpf"]] = dados 
    return dados

def buscar_participante():   
    dados = form("Nome", "Cpf", "Idade", "Email", "Telefone")
    participantes[dados["cpf"]] = dados 
    return dados
 
