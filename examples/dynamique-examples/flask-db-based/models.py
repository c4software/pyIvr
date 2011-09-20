from sqlalchemy import Column, Integer, Text
from database import Base

class demo(Base):
	__tablename__ = 'champ'
	id = Column(Integer, primary_key=True)
	value = Column(Text)

	def __init__(self, value=''):
		self.value = value

	def __repr__(self):
		return '<demo %r>' % (self.value)
	
