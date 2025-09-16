num = int(input("Enter a number less than 25: "))
if num < 25:
    print(num)
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1
else:
    print("Error")
