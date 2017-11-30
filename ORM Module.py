from sqlalchemy import Table, Column, String, Integer, create_engine, Float, NVARCHAR, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#it's important to add in SQL Server new database: ReportGenerator

"""
server=input('SERVER NAME: ')
database=input('DATABASE NAME: ')
driver=input('DRIVER NAME: ')
"""

Server='DOM'
Database='ReportGenerator'
Driver='SQL Server Native Client 11.0'

Engine = create_engine("mssql+pyodbc://"+Server+"/"+Database+"?driver="+Driver)

Base = declarative_base(bind=Engine)

class User(Base):
    __tablename__ = 'Users'
    ID = Column(Integer, primary_key=True)
    FIRST_NAME = Column(NVARCHAR(15))
    LAST_NAME = Column(NVARCHAR(15))
    CITY = Column(NVARCHAR(20))
    COUNTRY = Column(NVARCHAR(20))

    def __init__(self, FirstName, LastName, City, Country):
        self.FirstName = FirstName
        self.LastName = LastName
        self.City = City
        self.Country = Country

    def __repr__(self):
        return (self.FirstName,self.LastName,self.City,self.Country)


class Operation(Base):
    __tablename__ = 'Operations'
    ID = Column(Integer, primary_key=True)
    USER_ID = Column(Integer, ForeignKey('Users.ID'))
    DATE = Column(Date)
    TYPE = Column(NVARCHAR(6))
    VALUE = Column(Float)


    def __init__(self,Date,Type,Value):
        self.Date = Date
        self.Type = Type
        if Type=='D':
            self.Value = Value
        else:
            self.Value = -Value

    def __repr__(self):
        return (self.Date,self.Type,self.Value)

#New class Session? Using new class to commit all changes?

Meta = Base.metadata

Meta.create_all()

