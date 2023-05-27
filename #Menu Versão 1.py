#Menu Versão 1.1
import oracledb
import os
os.system('cls')
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
            opcao = int(input("Qual opção deseja escolher: "))
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
            print(row)
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
            print(row)
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
            print(row)
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
            print(row)
        # Deletando amostras
        apagar = int(input("Escolha um registro que sera apagado: "))
        cursor.execute(f"DELETE FROM amostras WHERE id = {apagar}")
        connection.commit()
        # Mostrando tabela
        print("Desta forma o banco de dados ficou assim:")
        cursor.execute("SELECT * FROM AMOSTRAS")
        res = cursor.fetchall()
        for row in res:
            print(row)
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
        print('\nResultado:\n')
        print(qualidade)
        input("\nPrecione qualquer tecla para continuar: ")
        os.system('cls')
    elif opcao == 5:
        break
    else:
        os.system('cls')
print("Obrigado por utilizar o sistema. Até a proxima!")