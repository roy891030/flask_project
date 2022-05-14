import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="roy891030891030",)

my_cursor = mydb.cursor()
my_cursor.execute("CREATE DATABASE index_name")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
