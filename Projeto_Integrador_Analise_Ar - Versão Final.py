#Menu Versão 1.1
import oracledb
import os
os.system('cls')
import numpy as np 
from numpy.linalg import inv

try:
    connection = oracledb.connect(
    user='bd240223113 ',
    password='Dyyzu9',
    dsn='172.16.12.14:1521/XE')
    print("Conexão com o banco de dados OK!!")
except:
    print("Ocorreu um erro na conexão, por favor verifique se no VPN esta atividado!!!")
cursor = connection.cursor()
print("Bem vindo ao sistema!!!")
while True:
    print("Por favor digite qual opção deseja utilizar!"
          "\nOpção 1 --- Inserir amostras"
          "\nOpção 2 --- Alterar amostras"
          "\nOpção 3 --- Deletar amostras"
          "\nOpção 4 --- Classificar amostras"
          "\nOpção 5 --- Sair")
    while True:
        try:
            opcao = int(input("Selecione uma opção: "))
            break
        except ValueError:
            print("Por favor digite um numero inteiro")
    if opcao == 1:
        # Inserção de dados
        os.system('cls')
        MP10 = float(input("Insira uma amostra MP10: "))
        while MP10 < 0:
            MP10 = float(input("Insira uma amostra positiva para MP10: "))
        MP2_5 = float(input("Insira uma amostra positiva para MP2,5: "))
        while MP2_5 < 0:
            MP2_5 = float(input("Insira uma amostra positiva para MP2,5: "))
        O3 = float(input("Insira uma amostra O3: "))
        while O3 < 0:
            O3 = float(input("Insira uma amostra positiva para O3: "))
        CO = float(input("Insira uma amostra CO: "))
        while CO < 0:
            CO = float(input("Insira uma amostra positiva para CO: "))
        NO2 = float(input("Insira uma amostra NO2: "))
        while NO2 < 0:
            NO2 = float(input("Insira uma amostra positiva para NO2: "))
        SO2 = float(input("Insira uma amostra SO2: "))
        while SO2 < 0:
            SO2 = float(input("Insira uma amostra positiva para SO2: "))
        cursor.execute("INSERT INTO amostras (MP10, MP2_5, O3, CO, NO2, SO2) VALUES (:val1, :val2, :val3, :val4, :val5, :val6)", 
                    {'val1': MP10, 'val2': MP2_5, 'val3': O3, 'val4': CO, 'val5': NO2, 'val6': SO2})
        # Salvando as alterações no banco de dados
        connection.commit()
        # Mostrando banco de dados
        print("\nAgora mostrarei como ficou o banco de dados!")
        cursor.execute("SELECT * FROM AMOSTRAS")
        res = cursor.fetchall()
        for row in res:
            print("ID: {}, MP10: {}, MP2_5: {}, O3: {}, CO: {}, NO2: {}, SO2: {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        # Limpando tela para retornar menu
        input("Pressione qualquer tecla para continuar...")
        os.system('cls')
    elif opcao == 2:
        # Alterando amostras
        os.system('cls')
        print('Irei mostrar os dados do banco para voce poder escolher qual deseja alterar')
        # Mostrando tabela
        cursor.execute("SELECT * FROM AMOSTRAS")
        res = cursor.fetchall()
        for row in res:
            print("ID: {}, MP10: {}, MP2_5: {}, O3: {}, CO: {}, NO2: {}, SO2: {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        # Inserindo novas amostras
        IDALT = float(input("Digite o id que deseja alterar: "))
        MP10ALT = float(input("Insira uma amostra MP10: "))
        while MP10ALT < 0:
            MP10ALT = float(input("Insira uma amostra positiva para MP10: "))
        MP2_5ALT = float(input("Insira uma amostra positiva para MP2,5: "))
        while MP2_5ALT < 0:
            MP2_5ALT = float(input("Insira uma amostra positiva para MP2,5: "))
        O3ALT = float(input("Insira uma amostra O3: "))
        while O3ALT < 0:
            O3ALT = float(input("Insira uma amostra positiva para O3: "))
        COALT = float(input("Insira uma amostra CO: "))
        while COALT < 0:
            COALT = float(input("Insira uma amostra positiva para CO: "))
        NO2ALT = float(input("Insira uma amostra NO2: "))
        while NO2ALT < 0:
            NO2ALT = float(input("Insira uma amostra positiva para NO2: "))
        SO2ALT = float(input("Insira uma amostra SO2: "))
        while SO2ALT < 0:
            SO2ALT = float(input("Insira uma amostra positiva para SO2: "))
        cursor = connection.cursor()
        consulta = cursor.execute(f"""
            UPDATE amostras
            set MP10 = {MP10ALT}, MP2_5 = {MP2_5ALT} , O3 = {O3ALT}, CO = {COALT}, NO2 = {NO2ALT}, SO2 = {SO2ALT}
            WHERE ID = {IDALT}
        """)
        print("Agora o banco de dados ficou desta forma:")
        # Mostrando banco
        cursor.execute("SELECT * FROM AMOSTRAS")
        res = cursor.fetchall()
        for row in res:
            print("ID: {}, MP10: {}, MP2_5: {}, O3: {}, CO: {}, NO2: {}, SO2: {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        # Salvando as alterações no banco de dados
        connection.commit()
        # Limpando tela para retornar menu
        input("Precione qualquer tecla para continuar: ")
        os.system('cls')
    elif opcao == 3:
        os.system('cls')
        # Mostrando tabela
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM AMOSTRAS")
        res = cursor.fetchall()
        for row in res:
            print("ID: {}, MP10: {}, MP2_5: {}, O3: {}, CO: {}, NO2: {}, SO2: {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        # Deletando amostras
        apagar = int(input("Escolha um registro que sera apagado: "))
        cursor.execute(f"DELETE FROM amostras WHERE id = {apagar}")
        connection.commit()
        # Mostrando tabela
        print("Desta forma o banco de dados ficou assim:")
        cursor.execute("SELECT * FROM AMOSTRAS")
        res = cursor.fetchall()
        for row in res:
            print("ID: {}, MP10: {}, MP2_5: {}, O3: {}, CO: {}, NO2: {}, SO2: {}".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        # Limpando tela para retorna menu
        input("Precione qualquer botão para continuar: ")
        os.system('cls')
    elif opcao == 4:
        os.system('cls')
        # Busca dos dados de média do BD
        cursor = connection.cursor()
        cursor.execute("SELECT AVG(MP10), AVG(MP2_5), AVG(O3), AVG(CO), AVG(NO2), AVG(SO2) FROM AMOSTRAS")
        res = cursor.fetchall()
        # Armazenando os valores das medias obtidos na lista res
        amostras = res[0]
        MP10 = amostras[0]
        MP2_5 = amostras[1]
        O3 = amostras[2]
        CO = amostras[3]
        NO2 = amostras[4]
        SO2 = amostras[5]
        print(f'Valores médios das amostras: MP10: {MP10:.2f} | MP2_5: {MP2_5:.2f} | O3: {O3:.2f} | CO: {CO:.2f} | NO2: {NO2:.2f} | SO2: {SO2:.2f}')
        # Classificando a qualidade do ar
        if MP10 > 250 or MP2_5 > 125 or O3 > 200 or CO > 15 or NO2 > 1130 or SO2 > 800:
            qualidade = 'Qualidade péssima.' '\nOs efeitos na saude são:' '\nToda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares.' \
                        '\nAumento de mortes prematuras em pessoas de grupos sensíveis.'
            ID_CRIPTO = 5
            
        elif MP10 > 150 or MP2_5 > 75 or O3 > 160 or CO > 13 or NO2 > 320 or SO2 > 365:
            qualidade = 'Qualidade muito ruim.' '\nOs efeitos na saide são:' '\nToda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante.' \
                        '\nEfeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).'
            ID_CRIPTO = 4
            
        elif MP10 > 100 or MP2_5 > 50 or O3 > 130 or CO > 11 or NO2 > 240 or SO2 > 40:
            qualidade = 'Qualidade ruim.' '\nOs efeitos na saude são:' '\nToda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta.' \
                        '\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.'
            ID_CRIPTO = 3
        elif MP10 > 50 or MP2_5 > 25 or O3 > 100 or CO > 9 or NO2 > 200 or SO2 > 20:
            qualidade = 'Qualidade moderada.' '\nOs efeitos na saude são:' 'Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço.' \
                    '\nA população, em geral, não é afetada.'
            ID_CRIPTO = 2
            
        else:
            qualidade = 'Qualidade boa.' '\nNão há efeitos à saúde.'
            ID_CRIPTO = 1
        
        ##Decodificação banco de dados:
        OPCAO_CRIPTOGRAFIA = True
        if OPCAO_CRIPTOGRAFIA:
            A = np.array(([16,21], [3,3])) #Chave A = PUCC
            tamanhoConjunto = 26
            dic = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 
                    11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 
                    20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 0:'Z'}
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
            cursor.execute(f"SELECT RESULTADO FROM CRIPTOGRAFIA WHERE ID_CRIPTO = {ID_CRIPTO}")
            resultado_consulta_cripto = cursor.fetchall()[0][0]
            connection.commit()
            #Chamada da funcao para converter a matriz texto em numeros
            resultado_consulta_cripto = textoParaNumero(resultado_consulta_cripto)
            #Chamada da funcao para montar a matriz de duas linhas 
            resultado_consulta_cripto = cria_matriz(resultado_consulta_cripto)
            matrizCriptografada_C = resultado_consulta_cripto
            #Valor do arredondamento da Determinante da matriz chave A
            det_A = round(np.linalg.det(A))
            #Criando e populando o Dicionario de Inverso do Z26, 
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
            #Algoritmo de Euclides:
            for i in P:
                ij = i%tamanhoConjunto
                P1.append(ij)
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
        
        print('\nResultado:\n')
        if OPCAO_CRIPTOGRAFIA: print(f'>>Resultado decodificado do Banco de Dados: {textoDecripto}\n')
        print(qualidade)
        input("\nPrecione qualquer tecla para continuar: ")
        os.system('cls')
    elif opcao == 5:
        break
    else:
        print("Por favor escolha uma opção de 1 ate 5")
        input("Precione qualquer tecla para continuar...")
        os.system('cls')
print("Obrigado por utilizar o sistema. Até a proxima!")