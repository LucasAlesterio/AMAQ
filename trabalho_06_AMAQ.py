import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv('sonar.csv',header=None)
import os
def clear():os.system('cls||clear')

def sigmoid(a,b):
    z=np.array(np.dot(a, b),dtype=np.float32)
    ans=1.0/(1.0+(np.exp(-1.0*z)))
    #print(ans)
    return ans
#R=0,M=1
def sigmoidDerivada(sig):
    return sig * (1 - sig)

x = np.array(data.values[:,0:59])
t = np.asmatrix(np.array(data.values[:,60])).T

neuronioEscondido = 25
neuronioSaida = 1
ciclosMax = 10000
a = 0.005

v = 2*np.random.random((len(x[0,:]),neuronioEscondido)) - 1
w = 2*np.random.random((neuronioEscondido,neuronioSaida)) - 1

ciclo = 1
porcentagem = 0
for j in range(ciclosMax):
    if(porcentagem != int((j*100)/ciclosMax)):
        clear()
        porcentagem = int((j*100)/ciclosMax)
        print('Treinando:',porcentagem,'%')
    camadaOculta = sigmoid(x,v)
    camadaSaida = sigmoid(camadaOculta,w)
    #erroCamadaSaida = t - camadaSaida
    erroCamadaSaida = np.array((t - camadaSaida),dtype=np.float32)
    #print(erroCamadaSaida)
    erroQuadratico = 0.5 * (erroCamadaSaida**2)
    mediaAbsoluta = np.mean(np.abs(erroQuadratico))
    #print("Erro: " + str(mediaAbsoluta))
    plt.scatter(j,mediaAbsoluta, color='orange', marker='.')
    derivadaSaida = sigmoidDerivada(camadaSaida)
    deltaSaida = erroCamadaSaida * derivadaSaida
    wTransposta = w.T
    deltaSaidaxPeso = deltaSaida.dot(wTransposta)
    deltaBv = deltaSaidaxPeso * sigmoidDerivada(camadaOculta)
    camadaOcultaTrasposta = camadaOculta.T
    deltinhaW = camadaOcultaTrasposta.dot(deltaSaida)
    w = (w * ciclo) + (deltinhaW * a)
    xTransposta = x.T
    deltinhaV = xTransposta.dot(deltaBv)
    v = (v * ciclo) + (deltinhaV * a)

print("W:")
print(w)
print("V:")
for i in range(len(v[:][0])):
    for j in range(len(v[0][:])):
        print('%.3f,'%(v[i][j]),end="")
    print("")
print("Erro: ")
print(str(mediaAbsoluta))
print("Camada de Saida:")
print(camadaSaida)
print("Teste da rede:")
print('---------- R ----------')
for i in range(96):
    if(camadaSaida[i]>0.5):
        print("M",end="")
    else:
        print("R",end="")
print("")
print('---------- M ----------')
for i in range(97,len(t)):
    if(camadaSaida[i]>0.5):
        print("M",end="")
    else:
        print("R",end="")
print("")
plt.show()

