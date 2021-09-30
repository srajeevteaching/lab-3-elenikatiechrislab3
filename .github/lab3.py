# Programmers: Katie, Chris, Eleni
# Course: CS151, Dr. Rajeev
# September 30, 2021
# Lab 3
package_weight = input("Enter the weight of the package in kg")
package_weight = float(package_weight)
travel_distance = input("Enter travel distance in miles")
travel_distance = float(travel_distance)
if package_weight > 20 or package_weight < 0:
    print("Invalid package weight")
elif travel_distance > 3000 or travel_distance < 10:
    print("invalid travel distance")