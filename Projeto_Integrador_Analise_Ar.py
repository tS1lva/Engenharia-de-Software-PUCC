#ENTREGA 01 PROGRAMA DE PROJETO INTEGRADOR

#Declaração da string da qualidade do ar vazia
qualidade = ''

#ENTRADAS - Inserção das amostras. Validação para que o usuário digite uma amostra válida (maior ou igual a zero)
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
               '\n A população, em geral, não é afetada.'
               
else:
    qualidade = 'Qualidade boa.' '\nNão há efeitos à saúde.'

#SAÍDA DA QUALIDADE DO AR E IMPLICAÇÕES NA SAÚDE
print('\nResultado:\n')
print(qualidade)
