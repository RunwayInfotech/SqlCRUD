
from datetime import datetime
from DatabaseHandler import DatabaseHandler

def test():
	databaseHandler = DatabaseHandler.OpenWithFile('../CredentialManager/credentials.xml', True)
	
	databaseHandler.CreateDatabase('testDb123')
	databaseHandler.SetDatabase('testDb123')
	
	name = 'table1'
	fields = [('field1', 'VARCHAR(50)'), ('field2', 'INTEGER'), ('timestamp', 'BIGINT')]
	
	databaseHandler.CreateTable(name, fields)
	
	dateTime = int(datetime.strptime('01-01-2010 10:00:00', '%d-%m-%Y %H:%M:%S').strftime('%s'))
	#print time.strftime('%d/%m/%y') # print today's date
	
	fields = ['field1', 'field2', 'timestamp']
	values = [['"hello"', 15, dateTime], ['"byebye"', 10, dateTime]]
	databaseHandler.InsertRecord(name, fields, values[0])
	databaseHandler.InsertRecord(name, fields, values[1])
	
	databaseHandler.SelectAll(name)
	databaseHandler.DeleteTable(name)
	databaseHandler.DeleteDatabase('testDb123')
	databaseHandler.CloseConnection()
            
test()
