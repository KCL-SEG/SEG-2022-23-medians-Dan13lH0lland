"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()
isEven = len(numbers) % 2
middle = len(numbers) // 2

if isEven == 0:
    middleValueOne = numbers[middle - 1]
    middleValueTwo = numbers[middle]
    median = (middleValueOne + middleValueTwo) / 2
    print(median)
else:
    print(numbers[middle])
