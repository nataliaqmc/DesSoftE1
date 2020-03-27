import random
fichas = 500

while fichas != 0:
print('Você possui {0} fichas.'.format(fichas))
continuar_ou_sair = input('Você deseja continuar as apostas ou sair do jogo?(Digite "continuar" ou "sair"):')
if continuar_ou_sair == "continuar":
    print('Você está na fase Come Out.')
    print('Você pode escolher entre quatro apostas, "Pass Line Bet", "Field", "Any Craps", ou "Twelve".')
    aposta_escolhida = input('Qual aposta você fará?:')
    if aposta_escolhida == "Pass Line Bet":
        valor_aposta = int(input('Qual o valor da aposta?'))
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        if (dado1 + dado2) == 7 or (dado1 + dado2) == 11:
            print('Você ganhou')
        elif (dado1 + dado2) == 2 or (dado1 + dado2) == 3 or (dado1 + dado2) == 12:
            print('Você perdeu')
        else:
            print('Agora você está na fase Point:')
            if 
        

