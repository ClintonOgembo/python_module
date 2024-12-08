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
