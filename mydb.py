import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass@123",
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE djangocrmdb")

print("All Done!")
