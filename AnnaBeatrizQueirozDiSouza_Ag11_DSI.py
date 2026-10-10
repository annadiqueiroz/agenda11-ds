from colorama import Fore, Style #importa a biblioteca colorama

niveis_agua = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
] #cria uma lista com os níveis de água

def definir_cor(nivel): #funçao que define a cor de acordo com o nivel de agua
    if nivel == 1:
        return Fore.RED
    if nivel == 2:
        return Fore.YELLOW
    if nivel == 3:
        return Fore.GREEN
    if nivel == 4:
        return Fore.CYAN
    if nivel == 5:
        return Fore.BLUE

def situacao_agua(nivel): #funcao que retorna de acordo com a lista criada anteriormente
    return niveis_agua[nivel-1] #ajusta o índice porque no python começa com índice 0

#Simulacao com os 5 niveis de água:
nivel_agua = 1
situacao = situacao_agua(nivel_agua)
cor = definir_cor(nivel_agua)

print(f"{cor}{situacao}") #retorna a cor de acordo com a funcao de cores definidas e a situacao definida na funcao situacao_agua

nivel_agua = 2
situacao = situacao_agua(nivel_agua)
cor = definir_cor(nivel_agua)

print(f"{cor}{situacao}")

nivel_agua = 3
situacao = situacao_agua(nivel_agua)
cor = definir_cor(nivel_agua)

print(f"{cor}{situacao}")

nivel_agua = 4
situacao = situacao_agua(nivel_agua)
cor = definir_cor(nivel_agua)

print(f"{cor}{situacao}")

nivel_agua = 5
situacao = situacao_agua(nivel_agua)
cor = definir_cor(nivel_agua)

print(f"{cor}{situacao}")

print(Style.RESET_ALL) #volta para a cor branca do terminal