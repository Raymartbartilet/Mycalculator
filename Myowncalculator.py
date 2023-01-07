# Get the user's input
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
operation = input("Enter an operation (+, -, *, /): ")

# Convert the input to numbers (we assume they are both integers in this example)
num1 = int(num1)
num2 = int(num2)

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

# Print the result
print(result)
