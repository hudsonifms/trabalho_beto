
import os

user = []

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
        try: #alterar isso
            if opcoes[inp-1][0] != None:
                func()
        except:
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
                listas = []
                while True:
                    limpar_terminal()
                    
                    print(f"---- {primeira_maiuscula(arg)} ----")
                    print("(pressione enter para finalizar)")

                    if len(listas) > 0:
                        for i in range(len(listas)):
                            print(f"{i+1}º - {listas[i]}")
                            
                    valor = input(f"{len(listas)+1}º - {primeira_maiuscula(arg)[:-1]}: ")

                    if not valor and len(listas) > 0:
                        break

                    if not validar(arg, valor) or not valor:
                        continue
                    listas.append(valor)

                valores[arg] = listas
            else:
                input_valor = input(f"{primeira_maiuscula(arg)}: ")
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
                print(f"{primeira_maiuscula(chave)}: \
                    {mostrar_dados(valor) if isinstance(valor, list) else valor}")

def continuar(mensagem="Pressione enter para continuar ... "):
    return input(mensagem)

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
        return len(valor) >= 10 and valor.isdigit()
    elif tipo == "idade":
        return valor.isdigit() and int(valor) > 0
    elif tipo == "palestrantes":
        return True

    if(len(valor) < 3):
        return False
    return True