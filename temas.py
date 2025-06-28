from util import *
 
temas = []

'''
    ID
    Título
    Descrição
'''

def menu_temas():
    opcoes = [
        [cadastrar_tema, "Cadastrar Tema"],
        [mostrar_temas, "Listar Temas"],
        [None, "Voltar"]
    ]

    mostrar_menu(opcoes, "---- [ TEMAS ] ----")
    tratar_input(menu_temas, opcoes, int(input("Escolha uma opção: ")))


def cadastrar_tema():
    limpar_terminal()
    print("---- CADASTRAR NOVO TEMA ----")
    
    if not dados['titulo'] or not dados['descricao']:
        print("Título e descrição são obrigatórios.")
        return continuar()
    
    dados = form("titulo", "descricao")
    temas.append(dados)
    
def mostrar_temas():
    limpar_terminal()
    print("---- LISTA DE TEMAS ----")
    if not temas:
        print("Nenhum tema cadastrado.")
        return continuar()
    
    for i, tema in enumerate(temas, start=1):
        print(f"{i} - {tema['titulo']}")

    inp = input("Escolha um tema ou pressione enter para voltar: ")
    
    if inp.isdigit() and 1 <= int(inp) <= len(temas):
        mostrar_dados(temas[int(inp) - 1])
        return continuar()
    
    if inp == "":
        return menu_temas()
    
    return mostrar_temas()

