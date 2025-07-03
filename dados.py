import json

arquivos = [
    "dados/temas.json",
    "dados/eventos.json",
    "dados/participantes.json"
]


def gerenciar_dados(nome_arquivo, variavel, tipo):
    if tipo == "w":
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(variavel, arquivo, ensure_ascii=False, indent=4)
    elif tipo == "r":
        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return None

def salvar_dados(temas, eventos, participantes):
    gerenciar_dados(arquivos[0], temas, "w")
    gerenciar_dados(arquivos[1], eventos, "w")
    gerenciar_dados(arquivos[2], participantes, "w")


def carregar_dados():
    dado = []
    for i in range(len(arquivos)):
        dado.append(gerenciar_dados(arquivos[i], None, "r"))
    return dado
