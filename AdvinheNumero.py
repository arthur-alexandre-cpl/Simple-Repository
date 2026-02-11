import random

numero = random.randint(1, 100)
acertou = False
tentativas = 0
while acertou == False and tentativas < 10:
    try: 
        valor = int(input('Digite um número de 1 à 100:  '))
        if valor < 1 or valor > 100:
            print('Apenas números entre 1 e 100.')
            continue
        tentativas += 1
        if valor > numero:
            print('Digite um número menor:  ')
        elif valor < numero:
            print('Digite um número maior:  ')
        else:
            print('Parabéns! Você acertou :) ')
            acertou = True
    except ValueError:
        print('Digite apenas números inteiros, amigo :/')
if not acertou:
    print(f'Você não conseguiu acertar. O número era: {numero}')