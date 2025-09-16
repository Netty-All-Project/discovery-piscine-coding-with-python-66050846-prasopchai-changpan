def add_one(n):
    """Takes a parameter and adds 1 to it."""
    n += 1
    print(f"Inside add_one: n = {n}")  # Print inside the function
    return n

# Initialize a variable in the body of the program
my_number = 5
print(f"Before calling add_one: my_number = {my_number}")

# Call the method that adds 1
add_one(my_number)

# Display your variable again in the body of the program
print(f"After calling add_one: my_number = {my_number}")

# What do you observe?
# The value of my_number remains unchanged after calling add_one.
# This is because add_one receives a copy of my_number, not the original variable itself.