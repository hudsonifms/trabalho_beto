from util import *
 
participantes = {}

participantes["12345678900"] = {
    "nome": "João Silva",
    "cpf": "12345678900",
    "idade": 30,
    "email": "joao.silva@email.com",
    "temas_preferidos": ["Python", "Data Science"]
}

participantes["98765432100"] = {
    "nome": "Maria Souza",
    "cpf": "98765432100",
    "idade": 25,
    "email": "maria.souza@email.com",
    "temas_preferidos": ["JavaScript", "Web Development"]
}
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
        [cadastrar_participante, "Cadastrar participantes"],
        [None, "Voltar"]
    ]

    mostrar_menu(opcoes, "---- [ PARTICIPANTES ] ----")
    tratar_input(menu_participantes, opcoes, int(input("Escolha a Opção: ")))


def cadastrar_participante():  
    print("---- NOVO PARTICIPANTE ----")
    dados = form("nome", "cpf", "idade", "email", "telefone")
    participantes[dados['cpf']] = dados
    
def buscar_participante():   
    print("---- BUSCA PARTICIPANTE ----")
    inp = input("Digite o cpf do participante: ")

    if(participantes[inp]):
        limpar_terminal()
        print("---- DADOS ----")
        mostrar_dados(participantes[inp])
        return continuar()
    
    return buscar_participante()
        
