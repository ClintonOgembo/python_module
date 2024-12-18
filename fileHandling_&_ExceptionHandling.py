# file handling
try:
    with open("nonexistent.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found. Please check the filename.")


try:
    file = open("sample.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()

# File Handling Example in Python

# 1. Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a simple file handling example.\n")
    file.write("Python makes it easy to work with files!")

print("File written successfully.")

# 2. Reading from the file
with open("example.txt", "r") as file:
    content = file.read()

print("\nContent of the file:")
print(content)

# 3. Appending to the file
with open("example.txt", "a") as file:
    file.write("\nThis line is added using append mode.")

print("\nLine appended successfully.")

# 4. Reading the updated file
with open("example.txt", "r") as file:
    updated_content = file.read()

print("\nUpdated content of the file:")
print(updated_content)
