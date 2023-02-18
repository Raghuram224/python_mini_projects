import mysql.connector

def connection():
	mydb = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	password = '',
	database = 'contacts'	
	)
	return mydb

def add_contact(first_name,last_name,phone_no):
	mydb=connection()
	my_cursor=mydb.cursor()

	sql = "INSERT INTO `table_contact`(`id`, `first name`, `last name`, `phone_no`) VALUES ('',%s,%s,%s);"
	val = (first_name,last_name,phone_no)

	my_cursor.execute(sql,val)
	mydb.commit()

	print( my_cursor.rowcount,'contact inserted')
	print()

def Show_contacts():
	mydb=connection()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM table_contact")

	myresult = mycursor.fetchall()
	for x in myresult:
		print(x)
	print()

def Delete_contact(delete_id):
	mydb=connection()
	my_cursor=mydb.cursor()

	sql = "DELETE FROM table_contact WHERE id ={}".format(delete_id)
	
	my_cursor.execute(sql)
	mydb.commit()
	

	