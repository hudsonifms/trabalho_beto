user = []

def mostrar_menu(opcoes, titulo=""):
    limpar_terminal()
    print(titulo)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao[1]}")

def tratar_input(func, opcoes, inp):
    try:
        user.append(opcoes[inp-1][0]())
    except:
        func()
    
def form(*args):
    valores = {}
    for arg in args:
        valores[arg] = input(f"Digite {arg}: ")
    return valores

def retornar_menu():
    menu = user[len(user)]
    user.pop()
    menu()
    
def limpar_terminal():
    for _ in range(20):
        print("")