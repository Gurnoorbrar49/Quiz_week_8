import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect('climate.db')
cursor = connection.cursor()

cursor.execute("SELECT year, co2, temperature FROM climate_data")

years = []
co2 = []
temp = []

for row in cursor.fetchall():
    year, co2_value, temp_value = row
    years.append(year)
    co2.append(co2_value)
    temp.append(temp_value)

connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.tight_layout() 

plt.savefig("co2_temp_1.png") 
plt.show()
