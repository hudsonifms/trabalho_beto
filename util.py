
import os

user = []
from datetime import datetime

def mostrar_menu(opcoes, titulo=""):
    limpar_terminal()
    print(titulo)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao[1]}")

def input_menu(func, opcoes, inp): 
    try:  
        inp = int(inp)
        limpar_terminal()
        user.append(opcoes[inp-1][0]())
        retornar_menu()
    except:
        if opcoes[inp-1][0] != None:
            func()
                
def formulario(*args, titulo="", lista=[]):
    valores = {}
    for arg in args:
        while validar(arg, valores.get(arg)) == False:
            if titulo:
                limpar_terminal()
                print(f"---- {titulo} ----")
                mostrar_dados(valores)
                
            if arg in lista:
                valores[arg] = []
                while True:
                    limpar_terminal()
                    print(f"---- {primeira_maiuscula(arg)} ----")
                    print("(pressione enter para finalizar)")

                    if len(valores[arg]) > 0:
                        for i in range(len(valores[arg])):
                            print(f"{i+1}º - {valores[arg][i]}")

                    valor = input(f"{len(valores[arg])+1}º - {primeira_maiuscula(arg)[:-1]}: ")

                    if not valor and len(valores[arg]) > 0:
                        break

                    if not validar(arg, valor) or not valor:
                        continue
                    valores[arg].append(valor)
            else:
                input_valor = input(f"{primeira_maiuscula(arg)}{mostrar_dica(arg)}: ")
                if validar(arg, input_valor) == False:
                    continue
                valores[arg] = input_valor
    return valores


def retornar_menu():
    menu = user[-1]
    user.pop()
    menu()
    
def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_dados(dados):
    if isinstance(dados, list):
        mensagem = ''
        for item in dados:
            mensagem += f"{primeira_maiuscula(item)}, "
        return mensagem[:-2]
    else:
        for chave, valor in dados.items():
            if(chave != "id"):
                print(f"{primeira_maiuscula(chave)}: {mostrar_dados(valor) if isinstance(valor, list) else valor}")


def continuar(mensagem="Pressione enter para continuar ... "):
    return input('\n'+mensagem)

def primeira_maiuscula(string):
    if not string:
        return ""
    return string[0].upper() + string[1:]

def validar(tipo, valor):
    if(valor is None):
        return False
    if tipo == "cpf":
        return len(valor) == 11 and valor.isdigit()
    elif tipo == "email":
        return "@" in valor and "." in valor
    elif tipo == "telefone":
        return len(valor) == 11 and valor.isdigit()
    elif tipo == "palestrantes":
        return True
    elif tipo == "data":
        try:
            datetime.strptime(valor, "%d/%m/%Y")
            return True
        except (ValueError, TypeError):
            return False
    if(len(valor) < 3):
        return False
    return True

def converter_data(data):
    try:
        return datetime.strptime(data, "%d/%m/%Y").strftime("%d-%m-%Y")
    except ValueError:
        return None
    
def limpar_printar(texto):
    limpar_terminal()
    print(texto)
    
def mostrar_dica(chave):
    dicas = {
        "cpf": " (somente números)",
        "email": " (exemplo@dominio.com)",
        "telefone": " (somente números, 11 dígitos)",
        "data": " (DD/MM/AAAA)"
    }
    return dicas.get(chave) or ""