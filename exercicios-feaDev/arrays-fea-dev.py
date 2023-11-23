import random
import time
import datetime
import pandas as pd
import numpy as np
def roleta():
    numeroCasa = random.randint(0,36)
    print('Rodando a roleta... Aguarde')
    time.sleep(0.2)
    print(f'A bola parou na casa {numeroCasa}')
    return numeroCasa

roleta()


#O verão está chegando e você já quer colocar uma caixa d´água na sua casa para usar como piscina. Na loja de materiais de construção, 
#o atendente informa que as caixas são vendidas em relação a área que a comporta, Sabendo que você tem um espaço para uma piscina de 5 metros de raio, 
#calcule a área do círculo, e descubra qual caixa comprar. 
#Lembre-se de que a fórmula para calcular a área de um círculo é A = π * r^2.
#Exercício 02

def raio():
    print('Informe o tamanho da piscina')
    tamanhoRaio = int(input(''))
    calculoRaio = 3.14*(tamanhoRaio**2)
    if calculoRaio >= 5:
        print(f'A piscina de tamanho {calculoRaio} é maior que o espaço disponível de 5M')
    else:
        print(F'A piscina de tamanho {calculoRaio} cabe no espaço disponível de 5M')

raio()


#Duvido você fazer um código que tenha como OUTPUT a data exata que você está fazendo essa questão. 
#Vamos descobrir se você é do tipo de pessoa que aproveita o dia para fazer as tarefas ou madruga para completa-las
#Exercício 03
hoje = datetime.date.today()
hora = datetime.datetime.now()
print(hoje)
print(hora)


#Você está fazendo uma rifa beneficiente para ajudar uma instituição de caridade do bairro. Está na hora de sortear quem é o grande vencedor de uma ALEXA 3º geração.

#Instruções:

#lista de nomes: nomes = ["Alice", "Bob", "Carlos", "Diana", "Eva","Henrique", "Isadora", "Leandro", "Patricia","Julia", "Alex"].

#Importe a biblioteca random.

#Use random.choice() para escolher aleatoriamente um nome da lista.

#Exiba o nome escolhido na tela.
#Exercício 04

listaDenomes = ["Alice", "Bob", "Carlos", "Diana", "Eva","Henrique", "Isadora", "Leandro", "Patricia","Julia", "Alex"]
print(f'O nome escolhido para ganhar a ALEXA 3ª Geração é: {random.choice(listaDenomes)}')


#Use o Pandas para ler os dados do arquivo CSV que está anexado à lista e criar um DataFrame.
#Além disso, vizualize somente as 5 primeiras linhas.

data = pd.read_csv('/10359%2F1698688206146-books2019file.csv')
print(type(data))