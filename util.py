
import os
from datetime import datetime

user = []

def mostrar_menu(opcoes, titulo=""):
    limpar_terminal()
    print(titulo)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao[1]}")


def confirmar_acao(lista, item):
    valor_input = ''
    while valor_input != 's' and valor_input != 'n':
        limpar_terminal()
        print(f"---- {lista.get('nome')} ----")
        mostrar_dados(lista)

        valor_input = input(f"\nDeseja cadastrar o {item}? (s(sim)/n(não)): ")
        if(valor_input == 's'):
            return True
        elif(valor_input == 'n'): 
            return False

def input_menu(funcao_anterior, opcoes, entrada): 
    try:  
        entrada = int(entrada)
        limpar_terminal()
        user.append(opcoes[entrada-1][0]())
        retornar_menu()
    except: # caso nao for inteiro
        try: #opcao voltar
            if opcoes[entrada-1][0] != None:
                funcao_anterior()
        except: #entrada vazia
            return funcao_anterior()
                
def formulario(*campos, titulo="", lista=[]):
    valores = {}
    for campo in campos:
        while validar(campo, valores.get(campo)) == False:
            if titulo:
                limpar_terminal()
                print(f"---- {titulo} ----")
                mostrar_dados(valores)
                
            if campo in lista:
                valores[campo] = []
                while True:
                    limpar_terminal()
                    print(f"---- {primeira_maiuscula(campo)} ----")
                    print("(pressione enter para finalizar)")

                    if len(valores[campo]) > 0:
                        for i in range(len(valores[campo])):
                            print(f"{i+1}º - {valores[campo][i]}")

                    valor = input(f"{len(valores[campo])+1}º - {primeira_maiuscula(campo)[:-1]}: ")

                    if not valor and len(valores[campo]) > 0:
                        break

                    if not validar(campo, valor) or not valor:
                        continue
                    valores[campo].append(valor)
            else:
                input_valor = input(f"{primeira_maiuscula(campo)}{mostrar_dica(campo)}: ")
                if validar(campo, input_valor) == False:
                    continue
                valores[campo] = input_valor
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