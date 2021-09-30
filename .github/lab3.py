# Programmers: Katie, Chris, Eleni
# Course: CS151, Dr. Rajeev
# September 30, 2021
# Lab 3
import sys
import math
package_weight = input("Enter the weight of the package in kg")
package_weight = float(package_weight)
if package_weight > 20 or package_weight < 0:
    print("Invalid package weight")
    sys.exit()
travel_distance = input("Enter travel distance in miles")
travel_distance = float(travel_distance)
if travel_distance > 3000 or travel_distance < 10:
    print("invalid travel distance")
    sys.exit

price = 0
price = float(price)
if package_weight <= 2:
    price = 1.10
elif package_weight > 2 and package_weight <= 6:
    price = 2.20
elif package_weight > 6 and package_weight <= 10:
    price = 3.70
elif package_weight > 10 and package_weight <= 20:
    price = 4.80

print(price)
