import oracledb
connection = oracledb.connect(
    user='User',
    password='senha',
    dsn='172.16.12.14:1521/XE')

print("Successfully connected to Oracle Database")
#ENTRADAS - Inserção das amostras. Validação para que o usuário digite uma amostra válida (maior ou igual a zero)
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


cursor = connection.cursor()
consulta = cursor.execute(f"""
    UPDATE amostras
    set MP10 = {MP10ALT}, MP2_5 = {MP2_5ALT} , O3 = {O3ALT}, CO = {COALT}, NO2 = {NO2ALT}, SO2 = {SO2ALT}
    WHERE ID = {IDALT}

""")

cursor.execute("SELECT * FROM AMOSTRAS")

res = cursor.fetchall()
for row in res:
    print(row)

cursor.close()

# Salvando as alterações no banco de dados
connection.commit()

# Fechando a conexão com o banco de dados
connection.close()
        