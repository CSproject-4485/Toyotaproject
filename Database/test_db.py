import sqlite3

#This makes the db everytime you compile
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE cars (
			vin_id integer,
			vin text,
			license_plate text)""")

def insert_car(car):
	with conn:
		c.execute("INSERT INTO cars VALUES (:vin_id, :vin, :license_plate)", {'vin_id': car.vin_id, 'vin': car.vin, 'license_plate': car.license_plate})

def get_car_by_vin(vin_look):
	c.execute("SELECT * FROM cars WHERE vin=:vin", {'vin': vin_look})

def remove_car(car):
	with conn:
		c.execute("DELETE from cars WHERE vin=:vin", {'vin': car.vin_id})


conn.close()