import pandas as pd
import sqlite3
conn = sqlite3.connect('../universal_datasets/log_file.sql')

df = pd.read_sql('''SELECT email, lat, long, date 
                    FROM customers 
                    WHERE name LIKE "%barry%"''', conn)

print(df.head(10))
