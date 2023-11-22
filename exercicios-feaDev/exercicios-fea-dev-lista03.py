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
    numeroSecreto = random.randint(1,100,5)
    print('Estes são os números secretos', numeroSecreto)
    while cont_loop <=3:
        print(f'Informe um número para advinhação entre 1 e 100, você tem 3 tentativas')
        numeroEscolhido = int(input())
        if cont_loop > 3:
            print('Tentativas esgotadas, programa encerrado')
            break
        elif numeroEscolhido != numeroSecreto:
            print(f'Você errou, você ainda tem {3- cont_loop} tentativas')
            cont_loop+=1
        elif numeroEscolhido == numeroSecreto:
            print('Parabéns, você acertou')
            break
numeroCerto()
    

#Desenvolva a função mult, que retorna a multiplicação dos parâmetros "a", "b", "c" e "d". Porém, a função não precisa necessariamente receber os 4 argumentos. 
#Caso um parâmetro não receba um argumento, ele deve valer 1.

def multValores(a=1, b=1, c=1, d=1): 
    result = (a * b * c * d)
    print(result)


multValores(2,2,2)


#Crie uma função chamada embaralhar_palavra que aceite uma palavra como argumento e retorne a mesma palavra com suas letras embaralhadas.
#Independentemente da entrada ser em maiúsculas ou minúsculas, a saída deve estar sempre em letras minúsculas.

def embaralhar():
    palavra = list(input('Informe uma palavra ').lower())
    random.shuffle(palavra)
    print(palavra)

embaralhar()


#Crie uma função chamada escolher_sabores que aceite uma lista de sabores de sorvete como argumento. 
#A função deve escolher aleatoriamente um sabor de sorvete da lista e retorná-lo.

sabores = list['Morango', 'Chocolate', 'Baunilha', 'Creme', 'Napolitano', 'Flocos']
def escolheSabor(sabores, *args):
    random.shuffle(args)

escolheSabor()