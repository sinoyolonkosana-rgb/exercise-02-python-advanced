# question 1 
import math


a = 5
b = 10
c = 7 

a += 3 
b *= 2
c %= 4
result = math.sqrt(a + b + c)
print(result)

# question 2 
x = int(input ("enter a number:"))
y = int(input ("enter another number:"))
z = int (input ("enter a third number:"))
is_even = (x % 2 == 0) and (y % 2 == 0) and (z % 2 == 0)
is_positive = y > 0
is_in_range = z >= 1 and z <= 100
final_condition = is_even and is_positive and is_in_range
print(f"Is even: {is_even}")
print(f"Is positive: {is_positive}")
print(f"Is in range: {is_in_range}")
print(f"Final condition: {final_condition}")

# question 3 

score = int(input ("Enter your score:"))
score += 5
score -= 10
score = max (0, score)
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"your grade is: {grade}")


print(f"your final score is: {score}")

# question 4
num1 = float(input(("Enter the first numer: ")))
num2 = float(input(("Enter the second number: ")))
operation = input("Enter the operation (+, -, *,/): ")
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
elif operation == "%":
    try:
        result = num1 % num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result: {result}")
elif operation == "**":
    result = num1 ** num2
    print(f"Result: {result}")
else:
    print("invalid operation. Please enter a valid operation (+, -, *, /, %, **).")

if operation in ("+", "-", "*"):
    print(f"Result: {result}")
