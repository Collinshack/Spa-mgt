import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'Admin',
    passwd = 'extraspa12$aaa'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE spas")

print('ooook')