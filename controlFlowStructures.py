# Conditional Statements
# Example of a basic if-elif-else statement

# Define the current temperature
temperature = 8

if temperature > 25:
    print("It's a hot day!")
elif temperature > 15:
    print("It's a warm day!")
elif temperature > 9:
    print("It's a cool day!")
else:
    print("It's a cold day!")

# Loops
# Example of a for loop

# List of fruits
fruits = ["apple", "banana", "cherry"]

# Loop through each fruit in the list
for fruit in fruits:
    print(f"I love {fruit}!")

# Example of a for loop with range

# Loop through numbers from 1 to 5
for number in range(1, 6):
    print(f"Number: {number}")

# Example of a while loop

# Initialize a counter
count = 1

# Loop while count is less than or equal to 5
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment the counter

# Example of loop controls: break and continue

# Loop through numbers from 1 to 9
for number in range(1, 10):
    if number == 5:
        print("Breaking the loop at 5")
        break  # Exit the loop when number is 5
    elif number % 2 == 0:
        print(f"Skipping {number} because it's even")
        continue  # Skip even numbers
    print(f"Processing number: {number}")

# Example of a nested loop

# Outer loop runs from 1 to 3
for i in range(1, 4):
    # Inner loop runs from 1 to 3
    for j in range(1, 4):
        print(f"Outer loop: {i}, Inner loop: {j}")

# Example of a do-while loop equivalent (using while True)

# Initialize a counter
counter = 1

# Loop indefinitely until the condition inside is met
while True:
    print(f"Counter is at: {counter}")
    counter += 1
    if counter > 5:
        break  # Exit the loop when counter exceeds 5

# Functions

# Define a simple function to greet a user
def greet(name):
    return f'Hello, {name}'

# Call the greet function
print(greet('Clinton'))

# Else with loops: Executes only if the loop completes without a break
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Exception Handling

# Example of a try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Example of a try-except-else block
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")

# Example of a try-finally block
try:
    result = 10 / 2
finally:
    print("Execution finished")

# Real-world Example: Simple Login System

# Define correct username and password
correct_username = "Clinton OG"
correct_password = "JacOb@254!*"

# Initialize authentication status
is_authenticated = False

# Loop until the user provides correct credentials
while not is_authenticated:
    # Get username and password input from the user
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the credentials match
    if username == correct_username and password == correct_password:
        print(f"Login successful! Welcome, {username}!")
        is_authenticated = True
    else:
        print("Invalid username or password. Please try again.\n")
