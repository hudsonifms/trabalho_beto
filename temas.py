from util import *
 
temas = []

'''
    id
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
    input_menu(menu_temas, opcoes, int(input("Escolha uma opção: ")))


def cadastrar_tema():
    limpar_terminal()
    print("---- CADASTRAR NOVO TEMA ----")
    
    if not dados['titulo'] or not dados['descricao']:
        print("Título e descrição são obrigatórios.")
        return continuar()
    
    dados = formulario("titulo", "descricao")
    temas.append(dados)
    
def mostrar_temas():
    limpar_terminal()
    print("---- LISTA DE TEMAS ----")
    if not temas:
        print("Nenhum tema cadastrado.")
        return continuar()
    
    listagem_temas = listar_temas()

    inp = input("Escolha um tema ou pressione enter para voltar: ")
    
    if inp.isdigit() and 1 <= int(inp) <= len(listagem_temas):
        limpar_terminal()
        print(f"---- {listagem_temas[int(inp) - 1]['titulo']} ----")
        mostrar_dados(listagem_temas[int(inp) - 1])
        return continuar()
    
    if inp == "":
        return menu_temas()
    
    return mostrar_temas()

def listar_temas(excluir_temas_listagem=""):
    temas_filtrados = [tema for tema in temas if tema['titulo'] not in excluir_temas_listagem]
    for i, tema in enumerate(temas_filtrados, start=1):
        print(f"{i} - {tema['titulo']}")

    return temas_filtrados