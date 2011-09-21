from sqlalchemy import Column, Integer, Text, String
from database import Base

class demo(Base):
	__tablename__ = 'demo'
	id = Column(Integer, primary_key=True)
	number = Column(String(50))
	value = Column(Text)

	def __init__(self, number='', value=''):
		self.value = value
		self.number = number

	def __repr__(self):
		return '<demo %r>' % (self.value)
	
