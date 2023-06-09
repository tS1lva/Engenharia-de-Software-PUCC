#CRIPTOGRAFIA
import numpy as np 
from numpy.linalg import inv
A = np.array(([16,21], [3,3])) #Chave A = PUCC

dic = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 
       11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 
       20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 0:'Z'}

tamanhoConjunto = 26

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

def cria_matriz(numeros):
    #Cria uma array com os números recebidos
    msgEmArray = np.array(numeros)
    
    msgDivPor2 = int(msgEmArray.size/2)
    matrizIndexImpar = []
    matrizIndexPar = []
        
    #Cria primeira linha, matriz de index ímpares
    for i in range(1, msgDivPor2+1):
        k = 2 * i - 1
        matrizIndexImpar.append(msgEmArray[k-1]) 

    #Segunda linha, matriz de index pares
    for i in range(1, msgDivPor2+1):
        k = 2 * i - 1
        matrizIndexPar.append(msgEmArray[k]) 

    #Criação da matriz P, juntando as duas linhas
    CLinha1 = np.array(matrizIndexImpar)
    CLinha2 = np.array(matrizIndexPar)
    P = np.vstack((CLinha1,CLinha2))
    
    return P

#RESULTADOS CLASSIFICAÇÃO AR PADRÃO: BOA, MODERADA, RUIM, MUITORUIM, PESSIMA
lista_resultados = ['VINICIUS','MODERADA','RUIM','MUITORUIM','PESSIMA']
lista_resultados_cripto = [] 

for i in range(len(lista_resultados)):
    msg = lista_resultados[i]
    
    #Chamada da funcao que converte texto em numeros
    msgEmNumero = textoParaNumero(msg)
    
    #Chamada da funcao que cria a matriz a partir dos numeros
    P = cria_matriz(msgEmNumero)

    #Criptografia da Matrix C = A * P
    C = np.dot(A, P)

    #Algoritmo de Euclides:
    C1 = [] 
    for i in C:
        ij = i % tamanhoConjunto
        C1.append(ij)

    #Montando a nova matriz C após aplicar Euclides
    CLinha1 = np.array(C1[0])
    CLinha2 = np.array(C1[1])
    C = np.vstack((CLinha1,CLinha2))
    matrizCriptografada_C = C
    
    #Matriz C e forma de Array linha e transformar numeros em texto
    matrizTransposta = np.transpose(C)
    C = np.hstack(matrizTransposta)
    #Chamada da funcao de numero para texto
    textoCripto = numeroParaTexto(C)

    print('-'*30)
    print('Matriz criptografada: ')
    print(matrizCriptografada_C)
    print(f'\nMensagem Criptografada: \n{textoCripto}')
    print('-'*30)
    #Alimenta a lista de mensagens criptografadas
    lista_resultados_cripto.append(textoCripto)

#############################################################################
#ORACLE
import oracledb
try:
    connection = oracledb.connect(
    user='bd240223113 ',
    password='Dyyzu9',
    dsn='172.16.12.14:1521/XE')
    print("Conexão com o banco de dados OK!!")
    
    cursor = connection.cursor()

    #cursor.execute("DELETE FROM CRIPTOGRAFIA")
      
    cursor.execute("INSERT INTO CRIPTOGRAFIA(ID_CRIPTO, RESULTADO) VALUES (1, :C1)", 
                {'C1': lista_resultados_cripto[0]})      
    cursor.execute("INSERT INTO CRIPTOGRAFIA(ID_CRIPTO, RESULTADO) VALUES (2, :C2)", 
                {'C2': lista_resultados_cripto[1]})     
    cursor.execute(f"INSERT INTO CRIPTOGRAFIA(ID_CRIPTO, RESULTADO) VALUES (3, :C3)", 
                {'C3': lista_resultados_cripto[2]}) 
    cursor.execute("INSERT INTO CRIPTOGRAFIA(ID_CRIPTO, RESULTADO) VALUES (4, :C4)", 
                {'C4': lista_resultados_cripto[3]}) 
    cursor.execute("INSERT INTO CRIPTOGRAFIA(ID_CRIPTO, RESULTADO) VALUES (5, :C5)", 
                {'C5': lista_resultados_cripto[4]})

    # Salvando as alterações no banco de dados
    connection.commit()
    
except:
    print("Ocorreu um erro na conexão, por favor verifique se no VPN esta atividado!!!")

#############################################################################
#DECODIFICAÇÃO
print('|'*50)
id_cripto_banco_de_dados = int(input('\nDigite o ID da mensagem que deseja decodificar: \n'))

cursor.execute(f"SELECT RESULTADO FROM CRIPTOGRAFIA WHERE ID_CRIPTO = {id_cripto_banco_de_dados}")
resultado_consulta_cripto = cursor.fetchall()[0][0]
connection.commit()
print('A mensagem criptografada seleciodada foi: ')
print(resultado_consulta_cripto)

#Chamada da funcao para converter a matriz texto em numeros
resultado_consulta_cripto = textoParaNumero(resultado_consulta_cripto)
#Chamada da funcao para montar a matriz de duas linhas 
resultado_consulta_cripto = cria_matriz(resultado_consulta_cripto)
matrizCriptografada_C = resultado_consulta_cripto

#Valor do arredondamento da Determinante da matriz chave A
det_A = round(np.linalg.det(A))

#Criando e populando o Dicionario de Inverso do Z26, 
#dicInv = {1:1, 9:3, 21:5, 15:7, 3:9, 19:11, 7:15, 23:17, 11:19, 5:21, 17:23, 25:25}
dicInv1 = {}
for i in range(1, tamanhoConjunto):
    dicInv1[i] = (det_A * i) % tamanhoConjunto

#Encontra o valor Inverso da determinante no dicionário. O valor que corresponder a 1
for i,j in dicInv1.items():
    if j == 1:
        det_A = i

#Montando a matriz A1 invertida através a matriz original A
A1 = np.array((  [A[1][1] , -A[0][1]]  ,  [-A[1][0] , A[0][0]]  ))

#Por fim o calculo da matriz Inversa A^-1 = det(A) * A
inv_A = det_A * (A1)

# P = A^-1 * C
P = np.dot(inv_A, matrizCriptografada_C)
P1 = []

print('antes euclides')
print(P)
#Algoritmo de Euclides:
for i in P:
    ij = i%tamanhoConjunto
    P1.append(ij)
print('antes euclides')
print(P1)
#Monta a matriz decodificada de duas linhas
PLinha1 = np.array(P1[0])
PLinha2 = np.array(P1[1])
P1 = np.vstack((PLinha1, PLinha2))
matrizDecodificada = P1

#Transposta da matriz P1
matrizTranspostaP1 = np.transpose(P1)
#Monta uma array linha com a matriz P1
P1 = np.hstack(matrizTranspostaP1)
#Chamada da funcao para transformar a array P1 em texto
textoDecripto = numeroParaTexto(P1)

print('\n>>>DECODIFICANDO...')
print('Matriz Decodificada: ')
print(matrizDecodificada)
print(f'\nMensagem Decodificada: \n{textoDecripto}')
print(' ')
