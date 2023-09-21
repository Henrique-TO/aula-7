import random

def Jogo():

    aleatorio= random.randint(1,25)
    chute= int(input('chute um numero'))

    if (aleatorio == chute):
        print('você acertou')

    elif chute != aleatorio :
        print ('tente novamente, era ' aleatorio)
    else:
        print('errou, o numero é', aleatorio)

 

Jogo()