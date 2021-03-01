# Declare variables
numberCount:int = 0
i:int = 0
userNumber:int = 0
average:float = 0
sumOfNumbers:float = 0

# Prompt user for the number of numbers to average
numberCount = eval(input("How many numbers are there to average? "))

# Retrieve and sum the numbers from user
for i in range(numberCount):
    print("Enter number %d of %d to be averaged: " % (i+1, numberCount), end=' ')
    userNumber = eval(input())
    sumOfNumbers = sumOfNumbers + userNumber
    print(sumOfNumbers)
    
# Calculate average
average = sumOfNumbers/numberCount

# Display average to user
print("\nThe average is %4.2f\n" % average)