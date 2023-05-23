#COMANDO PARA FAZER A CONEXÃO
import oracledb
con = oracledb.connect(
    user='bd240223113',
    password='Dyyzu9',
    dsn='172.16.12.14:1521/XE')

print("Successfully connected to Oracle Database")

cur = con.cursor()

cur.execute("select * from AMOSTRAS")

res = cur.fetchall()

for row in res:

    print(row)
#Declaração da string da qualidade do ar vazia

qualidade = ''

#Declarando clear e pause
import os
def clear():

    os.system('cls' if os.name == 'nt' else 'clear')
def pause():
    os.system('pause')

#Busca dos dados de média do BD
cur.execute("SELECT AVG(MP10), AVG(MP2_5), AVG(O3), AVG(CO), AVG(NO2), AVG(SO2) FROM AMOSTRAS")
res = cur.fetchall()

#Armazena os resultados na lista amostras e posteriormente nas respectivas variáveis
amostras = res[0]
MP10 = amostras[0]
MP2_5 = amostras[1]
O3 = amostras[2]
CO = amostras[3]
NO2 = amostras[4]
SO2 = amostras[5]

#Sistema do menu


while True:


    opcao = int(input('Escolha a opção do que deseja fazer:\n1 - Adicionar amostra\n2 - Alterar amostra\n3 - Apagar amostra\n4 - Classificar amostra\n5 - Sair do sistema:\n'))


    while opcao >= 6 or opcao <= 0:


        opcao = int(input('Insira uma opção valida!!!'))



    if opcao == 1:
        clear()


        print("Opção 1 - Adicionar amostra")
        pause()
        clear()


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

        cur.execute("INSERT INTO amostras (MP10, MP2_5, O3, CO, NO2, SO2) VALUES (:val1, :val2, :val3, :val4, :val5, :val6)",
               {'val1': MP10, 'val2': MP2_5, 'val3': O3, 'val4': CO, 'val5': NO2, 'val6': SO2})
        con.commit()
        print('Amostra inserida com sucesso!')
        pause()

    elif opcao == 2:
        clear()


        print('2 - Alterar amostra')
        pause()

        IDALT = float(input("Digite o id que deseja alterar"))
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
        cur = con.cursor()
        consulta = cur.execute(f"""
            UPDATE amostras
            set MP10 = {MP10ALT}, MP2_5 = {MP2_5ALT} , O3 = {O3ALT}, CO = {COALT}, NO2 = {NO2ALT}, SO2 = {SO2ALT}
            WHERE ID = {IDALT}
        """)
        cur.execute("SELECT * FROM AMOSTRAS")
        res = cur.fetchall()
        for row in res:
            print(row)
        cur.close()
        # Salvando as alterações no banco de dados
        con.commit()
        print('Amostra alterada com sucesso!')
        pause()
        
    elif opcao == 3:
        clear()
        print('3 - Apagar amostra')
        pause()
        clear()
        apagar = int(input("Escolha um registro que sera apagado: "))
        cur.execute(f"DELETE FROM amostras WHERE id = {apagar}")

        cur.close()

        # Salvando as alterações no banco de dados
        con.commit()
        print('Deletado com sucesso!')
        pause()
    
    elif opcao == 4:
        clear()
        print('4 - Classificar amostra')
        pause()
        clear()
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

        print(f'Valores médios das amostras: MP10: {MP10:.2f} | MP2_5: {MP2_5:.2f} | O3: {O3:.2f} | CO: {CO:.2f} | NO2: {NO2:.2f} | SO2: {SO2:.2f}')
        print('\nResultado:\n')
        print(qualidade)
        pause()
        clear()
    elif opcao == 5:

        print('Você esta saindo do programa!')
        con.close()
        exit()

