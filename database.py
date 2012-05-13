from sqlalchemy import *

class Database:
	def __init__(self, connectionString):
		self.connectionString = connectionString
		self.engine = create_engine(connectionString)
		self.metadata = MetaData()
		self.metadata.bind = self.engine
	
