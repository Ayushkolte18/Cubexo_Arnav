import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    database="tender_scrap",
    password='',

)

mysql_select_Query = "select * from master_database"
cursor = connection.cursor()
cursor.execute(mysql_select_Query)
records = cursor.fetchall()
mysql_select_Query1 = "select * from daily_database"
cursor1 = connection.cursor()
cursor1.execute(mysql_select_Query1)
records1 = cursor1.fetchall()
#print(records1)
