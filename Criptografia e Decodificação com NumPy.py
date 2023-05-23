import numpy as np 
from numpy.linalg import inv

C = np.array(([4,3], [1,2]))
D = inv(C)

dic = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 
       11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 
       21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 0:'Z'}

def textoParaNumero(texto):
    num = []
    if(len(texto)%2 != 0):
        ultimaLetra = len(texto)-1
        texto = texto + texto[ultimaLetra]
    for ii in texto:
        for j in dic:
            if dic[j] == ii:
                num.append(j)
    return num

def numeroParaTexto(num):
    texto = ''
    for i in num:
        texto = texto + str(dic[round(i)])
    return texto

msg = 'DARKNIGHT'

msgEmNumero = textoParaNumero(msg)

msgEmArray = np.array(msgEmNumero)

tamMsg = int(msgEmArray.size/2)

matrizIndexImpar = []
for i in range(1, tamMsg+1):
    k = 2 * i - 1
    matrizIndexImpar.append(msgEmArray[k-1]) 

matrizIndexPar = []
for i in range(1, tamMsg+1):
    k = 2 * i - 1
    matrizIndexPar.append(msgEmArray[k]) 

msgEmArray.reshape(2, tamMsg)

novaMatrix = []

linha1 = np.array(matrizIndexImpar)
linha2 = np.array(matrizIndexPar)

P = np.vstack((linha1,linha2))

E = np.dot(C, P)

#print(E)

F = []


for i in E:
    
    A = i%26
    #print(A)
    #A = int((abs((int(i/26)) - (i/26))*26))
    F.append(A)
    
    #E[i] = A
linha1 = np.array(F[0])
linha2 = np.array(F[1])
J = np.vstack((linha1,linha2))
#print(J)

textoLinha1 = numeroParaTexto(linha1)
textoLinha2 = numeroParaTexto(linha2)

cripto = np.vstack((textoLinha1,textoLinha2))

verprimeiralinha = cripto[0,:]

print(verprimeiralinha)