# Import the random module
import random

# Define a function to generate a random password
def generate_password(length, special, numbers):
  # Define the possible characters for the password
  lower = "abcdefghijklmnopqrstuvwxyz"
  upper = lower.upper()
  special = "!@#$%^&*()-_=+[]{};:,.<>/?"
  numbers = "0123456789"
  # Create an empty password
  password = ""
  # Create an empty list of characters to choose from
  chars = []
  # Add the lowercase letters to the list
  chars.extend(lower)
  # Check if the user wants special characters
  if special:
    # Add the special characters to the list
    chars.extend(special)
  # Check if the user wants numbers
  if numbers:
    # Add the numbers to the list
    chars.extend(numbers)
  # Loop for the length of the password
  for i in range(length):
    # Choose a random character from the list
    char = random.choice(chars)
    # Append the character to the password
    password += char
  # Return the password
  return password

# Ask the user to enter the password length
length = int(input("Enter the password length: "))
# Ask the user if they want special characters
special = input("Do you want special characters? (y/n): ")
# Convert the input to a boolean value
special = special.lower() == "y"
# Ask the user if they want numbers
numbers = input("Do you want numbers? (y/n): ")
# Convert the input to a boolean value
numbers = numbers.lower() == "y"
# Generate the password
password = generate_password(length, special, numbers)
# Print the password
print(f"Your password is: {password}")
