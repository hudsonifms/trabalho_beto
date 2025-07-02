import json
from temas import temas
from eventos import eventos
from participantes import participantes

arquivos = [
    ["dados/temas.json", temas],
    ["dados/eventos.json", eventos],
    ["dados/participantes.json", participantes]
]


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

def salvar_dados(**variaveis):
    for i in range(len(arquivos)):
        dados(arquivos[i][0], arquivos[i][1], "w")

def carregar_dados():
    dado = []
    for i in range(len(arquivos)):
        dado.append(dados(arquivos[i][0], None, "r"))
    return dado
