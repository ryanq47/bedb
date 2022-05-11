## This is a simple backend database program written in python
import os

def CreateDB(DB_name):
	os.mkdir("Database/" + DB_name) #0o777)
	## 0o644 allows creator to  read + write, but everyone else to only read. maybe in future make option to choose diff levels of security (640, 600 etc)
def CreateTABLE(DB_name,TABLE_name):
	os.mkdir("Database/"+ DB_name + '/' + TABLE_name)
	

def writeCOLUMN(DB_name,TABLE_name,COLUMN_name,COLUMN_contents):
	with open("Database/" + DB_name + '/' + TABLE_name + '/' + COLUMN_name, 'w') as c:
		c.write(COLUMN_contents)
	#Note this will overwrite existing file contents

def readCOLUMN(DB_name,TABLE_name,COLUMN_name):
	with open("Database/" + DB_name + '/' + TABLE_name + '/' + COLUMN_name) as r:
		print(r.read())
		#print(r.read()) -> for troubleshooting

