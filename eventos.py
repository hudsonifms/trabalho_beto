from util import *
from temas import *
from dados import gerenciar_dados

eventos = gerenciar_dados("dados/eventos.json", None, "r")


def menu_eventos():
    opcoes = [
        [cadastrar_evento, "Cadastrar Evento"],
        [mostrar_eventos, "Listar Eventos"],
        [menu_temas, "Temas"],
        [None, "Voltar"]
    ]

    mostrar_menu(opcoes, "---- [ EVENTOS ] ----")
    input_menu(menu_eventos, opcoes, int(input("Escolha uma opção: ")))


def cadastrar_evento():  
    if not temas:      
        return continuar("---- NOVO EVENTO ----\nNenhum tema cadastrado. Por favor, cadastre um tema primeiro.")

    dados = formulario("nome", "descricao", "local", "telefone", "data", "duracao", "palestrantes",titulo="NOVO EVENTO", lista=["palestrantes"])
    dados["id"] = len(eventos) + 1
    dados["tema"] = []
    dados["participantes"] = []
    
    while True:
        limpar_terminal()
        print("---- SELECIONAR TEMA ----\n(pressione enter para finalizar)")
        if(dados.get("tema")): print(f"Temas selecionados: {mostrar_dados(dados['tema'])}")
       
        listagem_temas = listar_temas(excluir_temas_listagem=dados.get("tema"))  
        inp = input("Escolha o tema (número): ")

        if inp.isdigit() and 1 <= int(inp) <= len(listagem_temas):
            dados["tema"].append(listagem_temas[int(inp) - 1]["titulo"])
            
        if inp == "" and len(dados.get("tema")) > 0:
            break

    
    limpar_terminal()
    print(f"---- [ {dados.get('nome')} ] ----")
    mostrar_dados(dados)

    if(confirmar_acao(dados, f"Deseja cadastrar o evento?") == True):
        eventos.append(dados)
        continuar("Cadastro concluido com sucesso! Pressione enter para continuar.")
    else: continuar("Cadastro cancelado! Pressione enter para continuar.")

 
def mostrar_eventos(filtros={}):
    limpar_terminal()
    print("---- LISTA DE EVENTOS ----")
    lista_eventos = listar_eventos(eventos, filtros)
    if not lista_eventos:
        print("Nenhum evento cadastrado.")
        return continuar()
    
    for i, evento in enumerate(lista_eventos, start=1):
        print(f"{i} - {evento['nome']}")
    
    inp = input("Escolha um evento (número) ou pressione enter para voltar: ")
    
    if inp.isdigit() and 1 <= int(inp) <= len(lista_eventos):
        limpar_terminal()
        print("---- DADOS DO EVENTO ----")
        mostrar_dados(lista_eventos[int(inp) - 1])
        return continuar()
    
    return menu_eventos()
  
def listar_eventos(lista, filtros={}):
    if filtros != {}:
        for key, value in filtros.items():
            filtrado = list(filter(lambda evento: value in evento.get(key), lista))
            lista = filtrado
    return lista

def mostrar_proximos_eventos(filtros={}):
    lista_eventos_filtrada = list(filter(lambda evento: datetime.now() < datetime.strptime(evento["data"], "%d/%m/%Y"), listar_eventos(eventos, filtros)))
    if not lista_eventos_filtrada:
        return continuar("Nenhum evento disponível para inscrição no momento... ")

    limpar_terminal()
    print("\n---- [ LISTA DE EVENTOS ] ----")
    for i, evento in enumerate(lista_eventos_filtrada, start=1):
        print(f"{i} - {evento['nome']} - Data: {evento['data']}")
    return lista_eventos_filtrada
