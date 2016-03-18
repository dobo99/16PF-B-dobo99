cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
# Above part is not printing but calculation for below part.
# '=' give a number to word. '_' connect word to word.


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "we need to put about", average_passengers_per_car, "in each car."
print ""
print "If 'space_in_a_car' has number 4,"
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
# Floating point has gone
print "we need to put about", average_passengers_per_car, "in each car."