import numpy as np
import numpy.matlib
import copy
import random

li=np.array([-1,-1])
ls=np.array([2,2])

tampop = 15
ng = 100
cr = 0.9
f = 0.5

aptidao_pop = np.zeros((tampop,1))
aptidao_trial = aptidao_pop
quant_var = len(li)
vet_trial = np.zeros((tampop,quant_var))

def rosenbrock(x):
    f = 0
    n = len(x)
    for i in range(n):
        f += (100 * ((x[i]-(x[i-1]**2))**2) + ((1 - x[i-1])**2))
    return f

pop = np.matlib.repmat(li,tampop,1) + np.matlib.repmat((ls-li),tampop,1)*np.random.random((tampop,quant_var))

for i in range(tampop):
    aptidao_pop[i][0] = rosenbrock(pop[i][:])

for t in range(ng):

    for i in range(tampop):
        b = copy.copy(list(pop))
        a = random.sample(b, 3)
        x1 = a[0]
        x2 = a[1]
        x3 = a[2]
        v = x1 + f * (x3-x2)
        delta = np.ceil(quant_var * np.random.random())

        for j in range(quant_var):
            if(np.random.random() <= cr or delta == j):
                vet_trial[i][j] = v[j]
            else:
                vet_trial[i][j] = pop[i][j]

    for j in range(tampop):
        vet_trial[j][:] = np.minimum(ls,vet_trial[j][:])
        vet_trial[j][:] = np.maximum(li,vet_trial[j][:])
        aptidao_trial[j] = rosenbrock(vet_trial[j][:])
        if(aptidao_trial[j] < aptidao_pop[j]):
            pop[j][:] = vet_trial[j][:]
            aptidao_pop[j] = aptidao_trial[j]

melhorFitness = min(aptidao_pop)
ind = np.argmin(aptidao_pop)
melhorSolucao = pop[ind][:]
print("Melhor solução: %.3f %.3f" %(melhorSolucao[0],melhorSolucao[1]))
print("Melhor fitness: %.3f" %(melhorFitness))
