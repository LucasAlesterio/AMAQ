entrada = [[1,1],[1,-1],[-1,1],[-1,-1]]
Entrada = [[' 1',' 1'],[' 1','-1'],['-1',' 1'],['-1','-1']]
limiar = 0
x=entrada
wNovo = [None,None]
bNovo = 0

#Treinamento
def treinar(y):
    wAnterior=[0,0]
    bAnterior = 0
    for i in range(len(entrada)):
        wNovo[0] = wAnterior[0] + x[i][0] * y[i]
        wNovo[1] = wAnterior[1] + x[i][1] * y[i]
        bNovo = bAnterior + y[i]
        wAnterior = wNovo
        bAnterior = bNovo

#Teste da rede treinada
def teste():
    saida = [1,1,1,-1]
    y=saida
    treinar(y)
    for i in range(len(entrada)):
        yLiquido = x[i][0] * wNovo[0] + x[i][1] * wNovo[1] + bNovo
        if yLiquido>=limiar:
            y=' 1'
        else:
            y='-1'
        print('|',Entrada[i][0],'|',Entrada[i][1],'|',y,'|')

    print('w:',wNovo[0],',',wNovo[1])

teste()

