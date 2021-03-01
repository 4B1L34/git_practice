# Program: rectangle.py
# Author : Abi Lea
# Course : CSC111
# Desc : this program will prompt the user for a length
# and width of rectangle and then calculate and print the area

# Declare the variable
length:float = 0.0          #input - length of rectangle
width: float = 0.0          #input - width of rectangle
area:float = 0.0           #output - area of rectangle
perimeter:float = 0.0       #output - perimeter of rectangle

# Declare length and width
length = eval(input("Please enter a valid positive length: "))
width = eval(input("Please enter a valid positive width: "))

# Check validity of length
while length < 0:
    print("Your rectangle is not real.")
    length = eval(input("Please enter a valid POSITIVE length: "))

# Check validity of width
while width < 0:
    print("Your rectangle is not real.")
    width = eval(input("Please enter a valid POSITIVE width: "))

# Calculate area
area = length * width

# Calculate perimeter
perimeter = (2.0*length) + (2.0*width)

# Print results
print("The area of your rectangle is %4.2f while the perimeter is %4.2f." % (area, perimeter)) 