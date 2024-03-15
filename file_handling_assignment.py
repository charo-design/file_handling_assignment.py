filename = "my_file.txt"

# **Reading the contents:**
try:
    with open(filename, "r") as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# **Appending to the file:**
try:
    with open(filename, "a") as file:
        file.write("\nMy name is Ann Charity.\n")
        file.write("\n+254700000000\n")
        file.write("\nCall me.\n")
    print(f"Successfully appended content to '{filename}'.")
except PermissionError:
    print(f"Error: Insufficient permissions to write to '{filename}'.")

# **Error handling demonstration (without file operations):**
try:
    # Simulate an error (replace with actual file operations)
    raise ValueError("This is a simulated error.")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("This block always executes, regardless of exceptions.")


