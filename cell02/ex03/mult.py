num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = int(num1) * int(num2)
print(f"{num1} x {num2} = {result}")
if result == 0:
    print("The result is zero.")
elif result < 0:
    print("The result is a negative number.")
else:
    print("The result is a positive number.")
