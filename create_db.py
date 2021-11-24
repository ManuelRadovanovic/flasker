import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    passwd = "YOUR-PASSWORD",
)

my_cursor = mydb.cursor()

# da slucajne se ne pokrene i kreira bazu
# my_cursor.execute("CREATE DATABASE users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

