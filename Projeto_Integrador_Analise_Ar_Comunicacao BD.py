import oracledb
import getpass

#pw = getpass.getpass("Enter password: ")

connection = oracledb.connect(
    user='bd240223112',
    password='Oosxb4',
    dsn='172.16.12.14:1521/XE')

print("Successfully connected to Oracle Database")

cursor = connection.cursor()
cursor.execute("select * from AMOSTRAS order by deptno")
res = cursor.fetchall()
cursor.close()
connection.close()





