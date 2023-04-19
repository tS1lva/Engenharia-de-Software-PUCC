import oracledb
import getpass

#pw = getpass.getpass("Enter password: ")

con = oracledb.connect(
    user='bd240223112',
    password='Oosxb4',
    dsn='172.16.12.14:1521/XE')

print("Successfully connected to Oracle Database")


cur = con.cursor()
cur.execute("select * from AMOSTRAS")
res = cur.fetchall()
for row in res:
    print(row)



