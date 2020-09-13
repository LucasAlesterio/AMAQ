import numpy as np
import matplotlib.pyplot as plt

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

x = np.array([[0,0],[0,1],[1,0],[1,1]])

t = np.array([[0], [1], [1], [0]])

v = 2*np.random.random((2,3)) - 1
w = 2*np.random.random((3,1)) - 1

ciclosMax = 15000
a = 0.1
ciclo = 1

for j in range(ciclosMax):
    somaSinapse0 = np.dot(x, v)
    camadaOculta = sigmoid(somaSinapse0)

    somaSinapse1 = np.dot(camadaOculta, w)
    camadaSaida = sigmoid(somaSinapse1)
    
    erroCamadaSaida = t - camadaSaida
    erroQuadratico = 0.5 * (erroCamadaSaida**2)
    mediaAbsoluta = np.mean(np.abs(erroQuadratico))
    print("Erro: " + str(mediaAbsoluta))
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

plt.show()
for i in range(0, 4):
    print(str(camadaSaida[i]))