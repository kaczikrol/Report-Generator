from sqlalchemy import Table, Column, String, Integer, create_engine, Float, NVARCHAR, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#it's important to add in SQL Server new database: ReportGenerator

"""
class Connection(sessionmaker):
    __Server='DOM'
    __Database='ReportGenerator'
    __Driver='SQL Server Native Client 11.0'
    Engine = create_engine("mssql+pyodbc://" + __Server + "/" + __Database + "?driver=" + __Driver)
    Base = declarative_base(bind=Engine)
    Meta = Base.metadata
    session = sessionmaker(bind=Engine)
    Session = session()

    def __init__(self):
        super().__init__(self)

    def add(self,**kwargs):
        super(Connection,self).add()

    def commit(self):
        super(Connection,self).commit()
"""

Engine=create_engine("mssql+pyodbc://DOM/ReportGenerator?driver=SQL Server Native Client 11.0")
Base = declarative_base(bind=Engine)
Meta = Base.metadata
Session = sessionmaker(bind=Engine)
session = Session()


class User(Base):
    __tablename__ = 'Users'
    Id = Column(Integer, primary_key=True)
    FirstName = Column(NVARCHAR(15))
    LastName = Column(NVARCHAR(15))
    City = Column(NVARCHAR(20))
    Country = Column(NVARCHAR(20))

    def __init__(self, FirstName, LastName, City, Country):
        self.FirstName = FirstName.upper()
        self.LastName = LastName.upper()
        self.City = City.upper()
        self.Country = Country.upper()

    def __repr__(self):
        return (self.FirstName,self.LastName,self.City,self.Country)


class Operation(Base):
    __tablename__ = 'Operations'
    Id = Column(Integer, primary_key=True)
    User_Id = Column(Integer, ForeignKey('Users.Id'))
    Date = Column(NVARCHAR(20))
    Type = Column(NVARCHAR(6))
    Value = Column(Float)
    Description = Column(NVARCHAR(30))


    def __init__(self,Date,Type,Value,Description):
        self.Date = Date
        self.Type = Type.upper()
        if Type=='D':
            self.Value = Value
        else:
            self.Value = -Value
        self.Description = Description

    def __repr__(self):
        return (self.Date,self.Type,self.Value,self.Description)


Meta.create_all()