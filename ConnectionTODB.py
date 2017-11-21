from sqlalchemy import create_engine

"""
import pyodbc
Connection via pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DOM;"
                      "Database=Northwind;"
                      "Trusted_Connection=yes;")


cursor = cnxn.cursor()
cursor.execute('SELECT CategoryID, CategoryName FROM Categories')

for row in cursor:
    print('row = %r' % (row,))

cnxn.close()
"""

engine = create_engine('mssql+pyodbc://DOM/Northwind?driver=SQL Server Native Client 11.0')
engine.connect()

print(engine.table_names())