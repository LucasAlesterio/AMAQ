from random import random
from decimal import Decimal
import matplotlib.pyplot as plt
import numpy as np

b1 = [
    [1.0,1.0],
    [1.1,1.5],
    [2.5,1.7],
    [1.0,2.0],
    [0.3,1.4],
    [2.8,1.0],
    [0.8,1.5],
    [2.5,0.5],
    [2.3,1.0],
    [0.5,1.1],
    [1.9,1.3],
    [2.0,0.9],
    [0.5,1.8],
    [2.1,0.6]
]

t = [1,1,-1,1,1,-1,1,-1,-1,1,-1,-1,1,-1]

teta=0
alfa=0.01
tolerancia=0.00001
ciclosMax = 300

def treinamentoPerceptron():
    wAnt=[0,0]
    bAnt=0
    wNovo=wAnt
    bNovo=bAnt
    trocou=True
    ciclos=0
    while(trocou):
        trocou=False
        ciclos+=1
        print('Ciclos %d' %(ciclos))
        for i in range(len(b1)):
            yLiquido = wAnt[0]*b1[i][0] + wAnt[1]*b1[i][1] + bAnt
            if(yLiquido >= teta):
                y=1
            else:
                y=-1
            if(y != t[i]):
                trocou = True
                wNovo[0] = wAnt[0] + alfa*b1[i][0]*t[i]
                wNovo[1] = wAnt[1] + alfa*b1[i][1]*t[i]
                bNovo = bAnt + alfa*t[i]
                wAnt = wNovo
                bAnt = bNovo
        print('wNovo: %f %f, bNovo: %f'%(wNovo[0],wNovo[1],bNovo))
    return [wAnt[0],wAnt[1],bAnt] 

def treinamentoAdaline():
    wAnt=[0.0,0.0]
    bAnt=0
    wAnt[0] = 0.5 - random()
    wAnt[1] = 0.5 - random()
    bAnt = 0.5 - random()
    wNovo=wAnt
    bNovo=bAnt
    trocou=True
    ciclos=0
    erroQuadratico = 0
    erros = []
    while(ciclos<=ciclosMax):
        ciclos += 1
        print('Ciclos %d' %(ciclos))
        for i in range(len(b1)):
            yLiquido = wAnt[0]*b1[i][0] + wAnt[1]*b1[i][1] + bAnt
            y=yLiquido
            erroQuadratico = ((Decimal(t[i])-Decimal(y))**2)*Decimal(1./2)
            wNovo[0] = wAnt[0] + alfa*b1[i][0]*(t[i] - y)
            wNovo[1] = wAnt[1] + alfa*b1[i][1]*(t[i] - y)
            bNovo = bAnt + alfa*(t[i] - y)
            wAnt = wNovo
            bAnt = bNovo
            if(erroQuadratico<=tolerancia):
                print('wNovo: %f %f, bNovo: %f, erro: %f'%(wNovo[0],wNovo[1],bNovo,erroQuadratico))
                return [wNovo[0],wNovo[1],bNovo,erros]
        #plt.scatter(ciclos,erroQuadratico,color='green', marker='.')
        erros.append(erroQuadratico)
        print('wNovo: %f %f, bNovo: %f, erro: %f'%(wNovo[0],wNovo[1],bNovo,erroQuadratico))

    return [wNovo[0],wNovo[1],bNovo,erros]

def teste(valores):
    wNovo=[0,0]
    wNovo[0] = valores[0]
    wNovo[1] = valores[1]
    bNovo = valores[2]
    for i in range(len(b1)):
        yLiquido = wNovo[0]*b1[i][0] + wNovo[1]*b1[i][1] + bNovo
        if(yLiquido >= teta):
            y = 1
        else:
            y =- 1
        print('x1:  %f,x2:  %f,y:   %d'%(b1[i][0],b1[i][1],y))

def grafico(valores):
    wNovo=[0,0]
    wNovo[0] = valores[0]
    wNovo[1] = valores[1]
    bNovo = valores[2]
    maiorX1 = b1[0][0]
    menorX1 = b1[0][0]

    for i in range(len(b1)):
        if(b1[i][0]>maiorX1):
            maiorX1 = b1[i][0]

        if(b1[i][0]<menorX1):
            menorX1 = b1[i][0]
        if(t[i]==1):
            plt.scatter(b1[i][0],b1[i][1], color='blue', marker='*')
        else:
            plt.scatter(b1[i][0],b1[i][1], color='red', marker='*')

    pontoA = [menorX1,0]
    pontoA[1] = ((-pontoA[0]*wNovo[0])-bNovo)/wNovo[1]

    pontoB = [maiorX1,0]
    pontoB[1] = ((-pontoB[0]*wNovo[0])-bNovo)/wNovo[1]

    plt.plot([pontoA[0],pontoB[0]],[pontoA[1],pontoB[1]], label='linear')
    plt.show()

def graficoErroQuadraticoAdaline():
    erros = treinamentoAdaline()[3]
    for i in range(len(erros)):
        plt.scatter(i,erros[i],color='orange', marker='.')
    plt.show()

alfa=0.4
#teste(treinamentoPerceptron())
#treinamentoAdaline()
#treinamentoPerceptron()
#teste(treinamentoAdaline())
#grafico(treinamentoAdaline())
graficoErroQuadraticoAdaline()
