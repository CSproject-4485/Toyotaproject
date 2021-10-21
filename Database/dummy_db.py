import sqlite3

import sqlite3
from parse import *
p1 = carObj(vin_string)


conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE cars(
            vin text
            )""")

conn.commit()

def insert_car(car):
	with conn:
		c.execute("INSERT INTO cars VALUES (:vin)", { 'vin': car.vin_num})

#c.executemany("INSERT INTO cars VALUES(:vin)", {"vin": p1.vin_num})

#conn.commit()
insert_car(p1)

c.execute("SELECT * FROM cars")

print(c.fetchall())

conn.commit()

conn.close()