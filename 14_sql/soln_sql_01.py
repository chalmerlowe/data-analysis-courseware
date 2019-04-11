import sqlite3
conn = sqlite3.connect('database01.db')

sql = '''CREATE TABLE villains (fname text,
                                lname text,
                                alias text,
                                age integer,
                                weapon text)'''
try:
    conn.execute(sql)
except:
    pass

cur = conn.cursor()

insert = '''INSERT INTO villains
            VALUES (?, ?, ?, ?, ?)'''

cur.execute(insert, ('harleen', 'quinzel', 'harley quinn', 32, 'bat'))

conn.commit()
conn.close()