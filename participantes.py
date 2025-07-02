from eventos import *
from util import *
 
participantes = {}
'''
{
    nome:
    cpf:
    email: 
    temas_preferidos:
}
'''
def menu_participantes():
    opcoes = [
        [inscrever_participante, "Inscrever Participante"],
        [cadastrar_participante, "Cadastrar participante"],
        [buscar_participante, "Buscar Participante"],
        [None, "Voltar"]
    ]

    mostrar_menu(opcoes, "---- [ PARTICIPANTES ] ----")
    input_menu(menu_participantes, opcoes, int(input("Escolha a Opção: ")))


def cadastrar_participante():  
    print("---- NOVO PARTICIPANTE ----")
    dados = formulario("nome", "cpf", "email", "telefone", titulo="CADASTRAR PARTICIPANTE")

    limpar_terminal()
    print(f"---- {dados.get('nome')} ----")
    mostrar_dados(dados)
    if(input("Deseja cadastrar participante? (s/qualquer tecla): ").lower() == "s"):
        if(dados['cpf'] in participantes):
            return continuar("CPF já cadastrado! Pressione enter para continuar.")
        participantes[dados['cpf']] = dados
        return continuar("Participante cadastrado com sucesso! Pressione enter para continuar.")
    return continuar("Cadastro cancelado! Pressione enter para continuar.")
    
def buscar_participante():   
    print("---- BUSCA PARTICIPANTE ----")
    inp = input("Digite o cpf do participante: ")

    if(participantes.get(inp)):
        limpar_terminal()
        print("---- DADOS ----")
        mostrar_dados(participantes[inp])
        return continuar()
    return buscar_participante()

def inscrever_participante():
    print("---- INSCRIÇÃO PARTICIPANTE ----")
    cpf = input("Digite o cpf do participante: ")

    if(participantes.get(cpf)):
        lista_eventos_filtrada = mostrar_proximos_eventos()
        escolha_evento = input("Escolha o evento para inscrição (número): ")
       
        if(escolha_evento.isdigit() and 1 <= int(escolha_evento) <= len(lista_eventos_filtrada)):
            if inserir_participante_evento(lista_eventos_filtrada[int(escolha_evento) - 1], cpf):
                return continuar("Participante inscrito com sucesso! Pressione enter para continuar... ")
            else:
                return continuar("Erro ao inscrever participante... ")
    return continuar("Participante não encontrado... ")

def inserir_participante_evento(evento, cpf):
    if not participantes.get(cpf) or not evento or cpf in evento.get("participantes"):
        return False   
    evento["participantes"].append(cpf)
    return True
        
