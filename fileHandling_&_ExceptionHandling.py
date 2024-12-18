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