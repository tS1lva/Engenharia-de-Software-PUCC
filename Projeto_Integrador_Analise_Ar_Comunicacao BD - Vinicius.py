import oracledb
# Comando para fazer a coneção

#ENTREGA 01 PROGRAMA DE PROJETO INTEGRADOR

#Declaração da string da qualidade do ar vazia
qualidade = ''

#ENTRADAS - Inserção das amostras. Validação para que o usuário digite uma amostra válida (maior ou igual a zero)

"""
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

"""


#ORACLE
connection = oracledb.connect(
    user='bd240223112',
    password='Oosxb4',
    dsn='172.16.12.14:1521/XE')

print("Successfully connected to Oracle Database")

cursor = connection.cursor()




# Comando para criar tabela no banco de dados

'''
cursor.execute("""
     create table amostras (
        id number generated always as identity,
        MP10 number(5),
        MP2_5 number(5),
        O3 number(5),
        CO number(5),
        NO2 number(5),
        SO2 number(5),
        primary key (id)
        )""")
'''



"""
cursor.execute("INSERT INTO amostras (MP10, MP2_5, O3, CO, NO2, SO2) VALUES (:val1, :val2, :val3, :val4, :val5, :val6)", 
               {'val1': MP10, 'val2': MP2_5, 'val3': O3, 'val4': CO, 'val5': NO2, 'val6': SO2})


"""
cursor.execute("SELECT * FROM AMOSTRAS WHERE ID =1")

res = cursor.fetchall()


for row in res:
    print(row)

cursor.close()



# Salvando as alterações no banco de dados
connection.commit()

# Fechando a conexão com o banco de dados
connection.close()
