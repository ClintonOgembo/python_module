# Example of a basic if statement
temperature = 8


if temperature > 25:
    print("It's a hot day!")
elif temperature > 15:
    print("It's a warm day!")
elif temperature > 9:
    print("It's a cool day!")
else:
    print("It's a cold day!")

# loops
# Example of a for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I love {fruit}!")

# Example of a for loop with range
for number in range(1, 6):  # Loops from 1 to 5
    print(f"Number: {number}")

# Example of a while loop
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1  # Increment the counter


# Example of loop controls: break and continue

for number in range(1, 10):  # Loop through numbers 1 to 9
    if number == 5:
        print("Breaking the loop at 5")
        break  # Exit the loop when number is 5
    elif number % 2 == 0:
        print(f"Skipping {number} because it's even")
        continue  # Skip the rest of the loop body for even numbers
    print(f"Processing number: {number}")


# Example of a nested loop
for i in range(1, 4):  # Outer loop
    for j in range(1, 4):  # Inner loop
        print(f"Outer loop: {i}, Inner loop: {j}")

# example of a do...while loop
counter = 1

while True:
    print(f"Counter is at: {counter}")
    counter += 1
    if counter > 5:
        break

# Exit a function and optionally return a value
def greet(name):
    return f'Hello, {name}'
print(greet('Clinton'))

# else with loops: executes only if the loop completes normally withoutb a break.
for i in range(5):
    print(i)
else:
    print("Loop completed")

# try-except: handles exceptions that may occur during runtime
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# try-except-else: excutes the else block if no exception occurs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful")

# try-except-finally: executes the finally block no matter what
try:
    result = 10 / 2
finally:
    print("Execution finished")


# Real world example
correct_username = "admin"
correct_password = "1234"
is_authenticated = False

while not is_authenticated:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == correct_username and password == correct_password:
        print(f"Login successful! Welcome, {username}!")
        is_authenticated = True
    else:
        print("Invalid username or password. Please try again.\n")
