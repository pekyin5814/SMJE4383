import math

#inserting the radius value
radius_str = input ("Enter the radius: ")
radius_int = int (radius_str)

#calculating the circumference and area
circum = 2 * math.pi * radius_int
area = math.pi * (radius_int ** 2)

#printing the area only
print (" the circumference is: ", circum, \
", and the area is: ", area)
