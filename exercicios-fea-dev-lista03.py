#Final do ano chegando e você já quer garantir sua viagem para a Europa, Crie uma função que converta valores euro para real. Considere que 1 euro equivale a 5.33 reais.
#Sabendo que hotel + comida + transporte + lazer darão entorno de 4500 euros, quantos reais você deverá guardar na sua poupança para garantir as férias.

#Exercício 0 converete o valor digitado em Euros para real 
def converteValor():
    """

    Função que converte o valor digitado em Euro para reis

    """
    print('Informe a quantidade de Euros para conversão')
    qntEuros = float(input())
    calculo = qntEuros * 5.33
    print(f'A quantidade de Euros de {qntEuros:.2f} equivale em reais é R$ {calculo:.2f}')
    return calculo

converteValor()

#Você está desenvolvendo um jogo de adivinhação muito simples, no qual o jogador tenta adivinhar um número secreto entre 1 e 100.
#**Instrução:**
#O programa gerará aleatoriamente um número entre 1 e 100 que o jogador deve adivinhar.
#O jogador poderá inserir um palpite (um número inteiro) e pressionar "Enter".
#O programa fornecerá feedback sobre o palpite do jogador, dizendo se o palpite é muito alto, muito baixo ou correto em relação ao número secreto.
#O jogador continuará a adivinhar até acertar o número secreto.
#O programa informará quantas tentativas foram necessárias para acertar o número.


import random
def numeroCerto():
    cont_loop = 1
    while cont_loop <=3:
        numeroSecreto = random.randint(1,100)
        print('Informe um número para advinhação entre 1 e 100, você tem 3 tentativas')
        numeroEscolhido = int(input())
        if cont_loop == 3:
            print('Tentativas esgotadas, progrma encerrado')
        elif numeroEscolhido != numeroSecreto:
            print(f'Você errou, você ainda tem {3- cont_loop} tentativas')
            cont_loop+=1
        else:
            print('Parabéns, você acrtou')
numeroCerto()
    