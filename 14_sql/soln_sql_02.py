import csv
fin = open('universal_datasets/villains.csv')
fin.readline()
fin.readline()
villaindata = csv.reader(fin)

import sqlite3
conn = sqlite3.connect('database01.db')
cur = conn.cursor()

insert = '''INSERT INTO villains
            VALUES (?, ?, ?, ?, ?)'''

for line in villaindata:
    firstname, lastname, weapon, age, alias = line
    cur.execute(insert, (firstname, lastname, alias, age, weapon))

conn.commit()