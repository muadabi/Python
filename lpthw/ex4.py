cars = 100 # assign an integer to a variable
spaceInACar = 4.0 # assign a floating-point to a variable
drivers = 30 # assign an integer to a variable
passengers = 90 # assign an integer to a variable
carsNotDriven = cars - drivers # it is performing a subtraction between two variables
                               # and it assigned to a variable
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
averagePassengersPerCar = passengers / carsDriven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", carsNotDriven, "empty cars today."
print "We can transport", carpoolCapacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", averagePassengersPerCar, " in each car."
