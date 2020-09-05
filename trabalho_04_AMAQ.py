from random import random
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np

dados = [
    [0.00,2.26],
    [0.50,3.80],
    [1.00,4.43],
    [1.50,5.91],
    [2.00,6.18],
    [2.50,7.26],
    [3.00,8.15],
    [3.50,9.14],
    [4.00,10.87],
    [4.50,11.58],
    [5.00,12.55]
]
teta = 0
alfa = 0.01
ciclosMax = 500

def treinamentoAdaline():
    wAnt = 0
    bAnt = 0
    wAnt = 0.5 - random()
    bAnt = 0.5 - random()
    wNovo = wAnt
    bNovo = bAnt
    ciclos = 0

    while(ciclos<=ciclosMax):
        ciclos += 1
        print('Ciclos %d' %(ciclos))
        for i in range(len(dados)):
            yLiquido = wAnt * dados[i][0] + bAnt
            y = yLiquido
            wNovo = wAnt + alfa * dados[i][0] * (dados[i][1] - y)
            bNovo = bAnt + alfa * (dados[i][1] - y)
            wAnt = wNovo
            bAnt = bNovo
        print('wNovo: %f, bNovo: %f' %(wNovo,bNovo))

    return [wNovo,bNovo]


def somatorios():
    somatorioXY = 0
    somatorioX = 0
    somatorioY = 0
    somatorioX2 = 0
    somatorioY2 = 0
    n = len(dados)

    for i in range(len(dados)):
        somatorioXY += dados[i][0] * dados[i][1]
        somatorioX += dados[i][0]
        somatorioY += dados[i][1]
        somatorioX2 += (dados[i][0]**2)
        somatorioY2 += (dados[i][1]**2)

    return [somatorioXY,somatorioX,somatorioY,somatorioX2,somatorioY2,n]


def regressao(resultado):
    somatorioXY = resultado[0]
    somatorioX = resultado[1]
    somatorioY = resultado[2]
    somatorioX2 = resultado[3]
    n = resultado[5]

    b = ((n * somatorioXY) - (somatorioX*somatorioY))/((n * somatorioX2)-(somatorioX**2))
    a = (somatorioY/n) - b*(somatorioX/n)

    print('a: %f, b: %f' %(a,b))


def coeficientes(resultado):
    somatorioXY = resultado[0]
    somatorioX = resultado[1]
    somatorioY = resultado[2]
    somatorioX2 = resultado[3]
    somatorioY2 = resultado[4]
    n = resultado[5]

    r = ((n * somatorioXY) - (somatorioX * somatorioY))/((((n * somatorioX2) - (somatorioX**2))**(1/2))*((((n * somatorioY2) - (somatorioY**2)))**(1/2)))
    determinacao = r ** 2
    
    print('Pearson: %f, Determinação: %f ' %(r,determinacao))


resultado = somatorios()
treinamentoAdaline()
regressao(resultado)
coeficientes(resultado)