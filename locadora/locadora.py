import os

def mostra_portfolio(carros):
    for i, car in enumerate(carros):
        print("[{}] {} - R$ {} / dia".format(i, car[0], car[1]))
        
def mostra_alugados(alugados):
    for i, car in enumerate(alugados):
        print("[{}] {} - R$ {} / dia".format(i, car[0], car[1]))


def aluga_carro(carros, alugados):
    
    print("==========")
    print("Escolha o código do carro:")
    cod = int(input())
    print("Escolha quantos dias deseja alugar:")
    dias = int(input())

    print("Você escolheu o {} por {} dia(s)".format(carros[cod][0], dias))

    print("O aluguel totalizaria R$ {}. Deseja alugar?".format(dias * carros[cod][1]))
    print("\n0 - SIM | 1 - NÃO")
    decisao = int(input())

    if decisao == 0:
        print("Parabéns você alugou o {} por {} dias".format(carros[cod][0], dias))
        alugados.append(carros.pop(cod))

def devolve_carros(carros,alugados):
    if alugados == []:
        print("\nNão há carros para devolver")
        return
        
    print("\nQual o código do carro que deseja devolver?")
    mostra_alugados(alugados)
    cod = int(input())
    carros.append(alugados.pop(cod))

opcao = 1

carros = [("Chevrolet Tracker", 120), ("Chevrolet Onix", 90), ("HB20", 100)]

alugados = []

while opcao == 1:
    print("Bem vindo à locadora Nunes")
    print("O que deseja fazer?")
    print("\n0 - Mostrar Portfólio, | 1 - Alugar um Carro | 2 - Devolver um carro")
    escolha = int(input())

    if escolha == 0:
        mostra_portfolio(carros)

    elif escolha == 1:
        mostra_portfolio(carros)
        aluga_carro(carros, alugados)        
        
    elif escolha == 2:
        devolve_carros(carros, alugados)
    
    print("\nDeseja continuar? 0 - Não 1 - Sim")
    opcao = int(input())
    os.system('cls')
