from util import *
from temas import *

eventos = []
'''
    id
    Data
    Local
    Descrição
    Lista de participantes (CPFs ou nomes)
    Lista de palestrantes
    Tema
    Telefone/contato
    Duração/horário
    Status (aberto, encerrado)
'''

eventos.append({
    "id": 1,
    "nome": "Workshop de Python",
    "data": "05-12-2024",
    "local": "Auditório Central",
    "descricao": "Evento introdutório sobre programação em Python.",
    "participantes": ["123.456.789-00", "Maria Silva"],
    "palestrantes": ["João Souza"],
    "tema": "Programação",
    "telefone": "(11) 99999-0001",
    "duracao": "09:00 - 12:00",
    "status": "aberto"
})
temas.append({
    "id": 1,
    "titulo": "Programação",
    "descricao": "Eventos relacionados a linguagens de programação."
})
eventos.append({
    "id": 2,
    "nome": "Seminário de IA",
    "data": "05-08-2024",
    "local": "Sala 101",
    "descricao": "Discussão sobre tendências em Inteligência Artificial.",
    "participantes": ["987.654.321-00", "Carlos Lima"],
    "palestrantes": ["Ana Paula"],
    "tema": "Inteligência Artificial",
    "telefone": "(21) 98888-1234",
    "duracao": "14:00 - 17:00",
    "status": "aberto"
})
 
eventos.append({
    "id": 3,
    "nome": "Seminário de IA",
    "data": "05-08-2026",
    "local": "Sala 101",
    "descricao": "Discussão sobre tendências em Inteligência Artificial.",
    "participantes": ["987.654.321-00", "Carlos Lima"],
    "palestrantes": ["Ana Paula"],
    "tema": "Inteligência Artificial",
    "telefone": "(21) 98888-1234",
    "duracao": "14:00 -  17:00",
 
})
 
 
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

    while True:
        limpar_terminal()
        print("---- SELECIONAR TEMA ----\n(pressione enter para finalizar)")
        if(dados.get("tema")): print(f"Temas selecionados: {mostrar_dados(dados['tema'])}")
       
        listagem_temas = listar_temas(excluir_temas_listagem=dados.get("tema"))  
        inp = input("Escolha o(s) tema(s): ")

        if inp.isdigit() and 1 <= int(inp) <= len(listagem_temas):
            dados["tema"].append(listagem_temas[int(inp) - 1]["titulo"])

        if inp == "" and len(dados.get("tema")) > 0:
            break

    limpar_terminal()
    print(f"---- {dados.get('nome')} ----")
    mostrar_dados(dados)
    if(input("Deseja criar o evento? (s/qualquer tecla): ").lower() == "s"):
        eventos.append(dados)
        return continuar("Evento cadastrado com sucesso! Pressione enter para continuar.")
    return continuar("Cadastro cancelado! Pressione enter para continuar.")
    
def mostrar_eventos():
    limpar_terminal()
    print("---- LISTA DE EVENTOS ----")
    eventos = listar_eventos(eventos)
    if not eventos:
        print("Nenhum evento cadastrado.")
        return continuar()
    
    for i, evento in enumerate(eventos, start=1):
        print(f"{i} - {evento['nome']}")
    
    inp = input("Escolha um evento ou pressione enter para voltar: ")
    
    if inp.isdigit() and 1 <= int(inp) <= len(eventos):
        limpar_terminal()
        print("---- DADOS DO EVENTO ----")
        mostrar_dados(eventos[int(inp) - 1])
        return continuar()
    
    return menu_eventos()
  
def listar_eventos(lista, filtros={}):
    if filtros != {}:
        for key, value in filtros.items():
            filtrado = list(filter(lambda evento: value in evento.get(key), lista))
            lista = filtrado
    return lista
