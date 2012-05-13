from database import *


class DocumentModel:
	def __init__(self):
		self.database = Database('mysql://root:dallas55@127.0.0.1:3306/crawler_persist')
		self.schema = Table('documents', self.database.metadata,
				Column('Id', Integer, primary_key=True),
				Column('Url', String(300)),
				mysql_engine='InnoDB',
				mysql_charset='utf8')
	def CreateTable(self):
		table = self.schema
		table.create()
	def RetrieveDocument(self, id):
		table = self.schema
		table.select(table.c.Id == id)
	def InsertLocation(self, url):
		table = self.schema
		table.insert().values(Url=url).execute()
