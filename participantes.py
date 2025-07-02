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
        participantes[dados['cpf']] = dados
        return continuar("Participante cadastrado com sucesso! Pressione enter para continuar.")
    return continuar("Cadastro cancelado! Pressione enter para continuar.")
    
def buscar_participante():   
    print("---- BUSCA PARTICIPANTE ----")
    inp = input("Digite o cpf do participante: ")

    if(participantes[inp]):
        limpar_terminal()
        print("---- DADOS ----")
        mostrar_dados(participantes[inp])
        return continuar()
    return buscar_participante()

def inscrever_participante():
    print("---- INSCRIÇÃO PARTICIPANTE ----")
    cpf = input("Digite o cpf do participante: ")

    if(participantes.get(cpf)):
        lista_eventos_filtrada = list(filter(lambda evento: datetime.now() < datetime.strptime(evento["data"], "%d-%m-%Y"), listar_eventos(eventos)))

        if not lista_eventos_filtrada:
            return continuar("Nenhum evento disponível para inscrição no momento... ")
       
        limpar_printar("\n---- LISTA DE EVENTOS ----")
        for i, evento in enumerate(lista_eventos_filtrada, start=1):
            print(f"{i} - {evento['nome']} - Data: {evento['data']}")
        escolha_evento = input("Escolha o evento para inscrição (número): ")

        if(escolha_evento.isdigit() and 1 <= int(escolha_evento) <= len(lista_eventos_filtrada)):
            if inserir_participante_evento(lista_eventos_filtrada[int(escolha_evento) - 1], cpf):
                return continuar("\nParticipante inscrito com sucesso! Pressione enter para continuar... ")
            else:
                return continuar("\nErro ao inscrever participante... ")
    return continuar("\nParticipante não encontrado... ")

def inserir_participante_evento(evento, cpf):
    if not participantes.get(cpf) or not evento or cpf in evento.get("participantes"):
        return False   
    evento["participantes"].append(cpf)
    return True
        
