'''
Exercício 1 de Design de Software - Insper
Jogo de Craps
@author: Natália Carreras
'''

import random
#Todo usuário começará o jogo com 500 fichas:
fichas = 500

#Início do jogo, fase 1- "Come Out":
while fichas != 0:
    print('Você possui {0} fichas.'.format(fichas))
    continuar_ou_sair = input('Você deseja continuar as apostas ou sair do jogo?(Digite "continuar" ou "sair"):')
    if continuar_ou_sair == "continuar":
        print('Você está na fase Come Out.')
        print('Você pode escolher entre quatro apostas, "Pass Line Bet", "Field", "Any Craps", ou "Twelve".')
        aposta_escolhida = input('Qual aposta você fará?:')
      #Pass Line Bet- fase 1:
        if aposta_escolhida == "Pass Line Bet":
            valor_aposta = int(input('Qual o valor da aposta?'))
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            somadados = dado1 + dado2
            if somadados == 7 or somadados == 11:
                print('Você ganhou!')
                fichas = fichas + valor_aposta
            elif somadados == 2 or somadados == 3 or somadados == 12:
                print('Você perdeu!')
                fichas = fichas - valor_aposta
            
            #Fase 2, "Point":
            else:
                print('Agora você está na fase Point:')
                print('Você pode escolher entre quatro apostas, "Pass Line Bet", "Field", "Any Craps", ou "Twelve".')
                aposta_escolhida = input('Qual aposta você fará?:')
                Point = somadados
                dado3 = random.randint(1,6)
                dado4 = random.randint(1,6)
                somadados2 = dado3 + dado4
              #Pass Line Bet- fase 2:
                if aposta_escolhida == 'Pass Line Bet':
                    Point = True
                    while Point:
                        if somadados2 != Point and somadados2 != 7:
                            print('Reiniciando fase Point: jogando os dados novamente!')
                            dado3 = random.randint(1,6)
                            dado4 = random.randint(1,6)
                            somadados2 = dado3 + dado4
                        elif somadados2 == Point:
                            print('Você ganhou!')
                            fichas = fichas + valor_aposta
                            Point = False
                        elif somadados2 == 7:
                            print('Você perdeu!')
                            fichas = 0
                            Point = False
              #Field- fase 2:
                elif aposta_escolhida == 'Field' :
                    dado1 = random.randint(1,6)
                    dado2 = random.randint(1,6)
                    somadados = dado1 + dado2
                    if somadados == 5 or somadados == 6 or somadados == 7 or somadados == 8:
                        print('Você perdeu tudo!')
                        fichas = 0
                    elif somadados == 2:
                        print('Você ganhou fichas em dobro!')
                        fichas = fichas + valor_aposta * 2
                    elif somadados == 12:
                        print('Você ganhou po triplo das fichas!')
                        fichas = fichas + valor_aposta * 3
                    else:
                        print('Você ganhou!')
                        fichas = fichas + valor_aposta
              #Any Craps- fase 2:
                elif aposta_escolhida == 'Any Craps':
                    dado1 = random.randint(1,6)
                    dado2 = random.randint(1,6)
                    somadados = dado1 + dado2
                    if somadados == 2 or somadados == 3 or somadados == 12:
                        print('Você ganhou sete vezes o valor das fichas apostadas!')
                        fichas = fichas + valor_aposta * 7
                    else:
                        print('Você perdeu!')
                        fichas = fichas - valor_aposta
              #Twelve - fase 2:
                elif aposta_escolhida == 'Twelve':
                    dado1 = random.randint(1,6)
                    dado2 = random.randint(1,6)
                    somadados = dado1 + dado2
                    if somadados == 12:
                        print('Você ganhou 30 vezes o valor de fichas apostado!')
                        fichas = fichas + valor_aposta * 30
                    else:
                        print('Você perdeu!')
                        fichas = fichas - valor_aposta
      #Field- fase 1:        
        elif aposta_escolhida == 'Field' :
            valor_aposta = int(input('Qual o valor da aposta?'))
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            somadados = dado1 + dado2
            if somadados == 5 or somadados == 6 or somadados == 7 or somadados == 8:
                print('Você perdeu tudo!')
                fichas = 0
            elif somadados == 2:
                print('Você ganhou fichas em dobro!')
                fichas = fichas + valor_aposta * 2
            elif somadados == 12:
                print('Você ganhou po triplo das fichas!')
                fichas = fichas + valor_aposta * 3
            else:
                print('Você ganhou!')
                fichas = fichas + valor_aposta
      #Any Craps- fase 1:
        elif aposta_escolhida == 'Any Craps':
            valor_aposta = int(input('Qual o valor da aposta?'))
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            somadados = dado1 + dado2
            if somadados == 2 or somadados == 3 or somadados == 12:
                print('Você ganhou sete vezes o valor das fichas apostadas!')
                fichas = fichas + valor_aposta * 7
            else:
                print('Você perdeu!')
                fichas = fichas - valor_aposta
      #Twelve- fase 1:
        elif aposta_escolhida == 'Twelve':
            valor_aposta = int(input('Qual o valor da aposta?'))
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            somadados = dado1 + dado2
            if somadados == 12:
                print('Você ganhou 30 vezes o valor de fichas apostado!')
                fichas = fichas + valor_aposta * 30
            else:
                print('Você perdeu!')
                fichas = fichas - valor_aposta
    else:
        break
print('GAME OVER!')

        

