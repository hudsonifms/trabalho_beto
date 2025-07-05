from eventos import *
from util import *
from dados import gerenciar_dados

participantes = gerenciar_dados("dados/participantes.json", None, "r")

def menu_participantes(cpf=-1):
    if(cpf == -1):
        return buscar_participante()

    participante_cpf = cpf
    if not participantes.get(participante_cpf):
        return continuar("Participante não encontrado... ")
 
    opcoes = [
        [lambda: inscrever_participante(cpf), "Inscrever em evento"],
        [lambda: dados_participantes(cpf), "Dados do participante"],
        [lambda: eventos_participante(cpf), "Eventos inscrito"],
        [None, "Voltar"]
    ]

    mostrar_menu(opcoes, "---- [ PARTICIPANTE ] ----")
    input_menu(menu_participantes, opcoes, int(input("Escolha a opção: ")))


def cadastrar_participante(cpf):  
    dados = formulario("nome", "email", "telefone", titulo="CADASTRO")
 
    if(confirmar_acao(dados, "Deseja cadastrar o participante?", titulo="CADASTRO") == True):
        dados["cpf"] = cpf
        if(dados["cpf"] in participantes):
            return continuar("CPF já cadastrado! Pressione enter para continuar.")

        participantes[dados["cpf"]] = dados
        mostrar_dados_participante(dados["cpf"], continuar=False)
        continuar("Participante cadastrado com sucesso! Pressione enter para continuar.")
        return menu_participantes(dados["cpf"])
    else: continuar("Cadastro cancelado! Pressione enter para continuar.")
 
def buscar_participante():   
    limpar_terminal()

    print("---- [ PARTICIPANTES ] ----\nInforme o CPF para cadastra-lo ou\ngerenciar participante já cadastrado.\n(pressione enter para voltar)")

    cpf = input("Digite o CPF (apenas números): ")
    if(cpf == ''):
        return

    if(participantes.get(cpf)):
        menu_participantes(cpf)
        
    else:
        if(confirmar_acao([], f"Participante não encontrado (CPF - {cpf}).\nDeseja cadastrar o participante?") == True):
            return cadastrar_participante(cpf)
        else: 
            return continuar("Cadastro cancelado! Pressione enter para continuar.")

def inscrever_participante(cpf=None):
    if(participantes.get(cpf)):
        lista_eventos_filtrada = mostrar_proximos_eventos()
        escolha_evento = input("Escolha o evento para inscrição (número): ")
       
        if(escolha_evento.isdigit() and 1 <= int(escolha_evento) <= len(lista_eventos_filtrada)):
            if inserir_participante_evento(lista_eventos_filtrada[int(escolha_evento) - 1], cpf):
                continuar("Participante inscrito com sucesso! Pressione enter para continuar... ")
                return menu_participantes(cpf)
            else:
                continuar("Erro ao inscrever participante... ")
                return menu_participantes(cpf)
        elif(escolha_evento == ""):
            return menu_participantes(cpf)
        else: inscrever_participante(cpf)
    else: return continuar("Participante não encontrado...  ")


def dados_participantes(cpf=None):
    if not participantes.get(cpf):
        return continuar("Participante não encontrado... ")
    
    limpar_terminal()
    print(f"---- [ PARTICIPANTE ] ----")
 
    if(confirmar_acao(participantes[cpf], "Deseja editar os dados do participante?", limpar=False) == True):
        dados = formulario("nome", "email", "telefone", titulo="EDIÇÃO")
        participantes[cpf].update(dados)
        mostrar_dados_participante(cpf, continuar=False)
        continuar("Dados atualizados com sucesso! Pressione enter para continuar... ")
    return menu_participantes(cpf)

def inserir_participante_evento(evento, cpf):
    if not evento or cpf in evento.get("participantes"):
        if(cpf in evento.get("participantes")):
            print("Participante já inscrito neste evento.")
        return False   
    evento["participantes"].append(cpf)
    return True

def eventos_participante(cpf=None):
    if not participantes.get(cpf):
        return continuar("Participante não encontrado... ")
    
    limpar_terminal()
    print(f"---- [ PROXIMOS EVENTOS INSCRITO ] ----")
    
    lista_eventos = listar_eventos(eventos, {"participantes": cpf})

    if not lista_eventos:
        print("Nenhum evento inscrito.")
        continuar("Pressione enter para continuar... ")
        return menu_participantes(cpf)
    
    mostrar_eventos({"participantes": cpf})
    inp = input("Escolha um evento (número) ou pressione enter para voltar: ")

    if inp == "":
        return menu_participantes(cpf)
    
    if inp.isdigit() and 1 <= int(inp) <= len(lista_eventos):
        limpar_terminal()
        print(f"---- [ {listar_eventos[int(inp) - 1]['nome']} ] ----")
        mostrar_dados(listar_eventos[int(inp) - 1])
        continuar("Pressione enter para voltar... ")
        return menu_participantes(cpf)
    return menu_participantes(cpf)

def mostrar_dados_participante(cpf=None, continuar=True):
    if not participantes.get(cpf):
        return continuar("Participante não encontrado... ")
    
    limpar_terminal()
    print(f"---- [ PARTICIPANTE ] ----")
    mostrar_dados(participantes[cpf])
    
    if(continuar == True): return continuar("Pressione enter para continuar... ")
    
# if __name__ == "__main__":
#     eventos_participante("12345678901")