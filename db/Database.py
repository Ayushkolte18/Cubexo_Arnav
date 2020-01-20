import mysql.connector

connection = mysql.connector.connect(
  host = "localhost",
  user = "root",
  database="tender_scrap",
  password ='',

)
print(connection)

sql_select_Query = "select * from master_database"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
for x in records:
  print("Total number of rows  is: ", x, "\n")
