import oracledb
connection = oracledb.connect(
    user='bd240223113',
    password='Dyyzu9',
    dsn='172.16.12.14:1521/XE')

print("Successfully connected to Oracle Database")

cursor = connection.cursor()
cursor.execute("SELECT * FROM AMOSTRAS")

res = cursor.fetchall()
for row in res:
    print(row)

apagar = int(input("Escolha um registro que sera apagado: "))
cursor.execute(f"DELETE FROM amostras WHERE id = {apagar}")

cursor.close()

# Salvando as alterações no banco de dados
connection.commit()

# Fechando a conexão com o banco de dados
connection.close()