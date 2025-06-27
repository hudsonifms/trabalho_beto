user = []

def mostrar_menu(opcoes, titulo=""):
    limpar_terminal()
    print(titulo)
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i} - {opcao[1]}")

def tratar_input(func, opcoes, inp): 
    try:  
        limpar_terminal()
        user.append(opcoes[inp-1][0]())
        retornar_menu()
    except:
        try: #alterar isso
            if opcoes[inp-1][0] != None:
                func()
        except:
            func()
            
def form(*args):
    valores = {}
    for arg in args:
        valores[arg] = input(f"Digite {arg}: ")
    return valores

def retornar_menu():
    menu = user[-1]
    user.pop()
    menu()
    
def limpar_terminal():
    for _ in range(20):
        print("")
        
def mostrar_dados(dados):
    for chave, valor in dados.items():
        # if(isinstance(valor, list)):
        #     for i in valor:
        #         if():
        #         print(f" {i}")
        print(f"{chave}: {valor}")
        
def continuar():
    return input("Pressione enter para continuar ")