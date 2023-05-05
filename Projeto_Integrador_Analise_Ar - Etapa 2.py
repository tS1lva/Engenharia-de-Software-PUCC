#ENTREGA 02 PROGRAMA DE PROJETO INTEGRADOR

#Declaração da string da qualidade do ar vazia
qualidade = ''

#ORACLE
import oracledb
connection = oracledb.connect(
    user='bd240223112',
    password='Oosxb4',
    dsn='172.16.12.14:1521/XE')

print("\nConexão com o Banco de Dados bem sucedida.\n\n")

#Busca dos dados de média do BD
cursor = connection.cursor()
cursor.execute("SELECT AVG(MP10), AVG(MP2_5), AVG(O3), AVG(CO), AVG(NO2), AVG(SO2) FROM AMOSTRAS")
res = cursor.fetchall()

#Armazena os resultados na lista amostras e posteriormente nas respectivas variáveis
amostras = res[0]
MP10 = amostras[0]
MP2_5 = amostras[1]
O3 = amostras[2]
CO = amostras[3]
NO2 = amostras[4]
SO2 = amostras[5]

#EXIBIR VALORES MEDIOS DAS AMOSTRAS
print(f'Valores médios das amostras: MP10: {MP10:.2f} | MP2_5: {MP2_5:.2f} | O3: {O3:.2f} | CO: {CO:.2f} | NO2: {NO2:.2f} | SO2: {SO2:.2f}')


#PROCESSAMENTO DA CLASSIFICAÇÃO DO AR E IMPLICAÇÕES NA SAÚDE
if MP10 > 250 or MP2_5 > 125 or O3 > 200 or CO > 15 or NO2 > 1130 or SO2 > 800:
    qualidade = 'Qualidade péssima.' '\nOs efeitos na saude são:' '\nToda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares.' \
                '\nAumento de mortes prematuras em pessoas de grupos sensíveis.'

elif MP10 > 150 or MP2_5 > 75 or O3 > 160 or CO > 13 or NO2 > 320 or SO2 > 365:
    qualidade = 'Qualidade muito ruim.' '\nOs efeitos na saide são:' '\nToda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante.' \
                '\nEfeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).'
                
elif MP10 > 100 or MP2_5 > 50 or O3 > 130 or CO > 11 or NO2 > 240 or SO2 > 40:
    qualidade = 'Qualidade ruim.' '\nOs efeitos na saude são:' '\nToda a população pode apresentar sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta.' \
                '\nPessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar efeitos mais sérios na saúde.'
                
elif MP10 > 50 or MP2_5 > 25 or O3 > 100 or CO > 9 or NO2 > 200 or SO2 > 20:
   qualidade = 'Qualidade moderada.' '\nOs efeitos na saude são:' 'Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço.' \
               '\nA população, em geral, não é afetada.'
               
else:
    qualidade = 'Qualidade boa.' '\nNão há efeitos à saúde.'

#SAÍDA DA QUALIDADE DO AR E IMPLICAÇÕES NA SAÚDE
print('\nResultado:\n')
print(qualidade)