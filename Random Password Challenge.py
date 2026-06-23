import string
import random

# Define the character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits

# Combine all characters
all_chars = lowercase + uppercase + digits

# Generate a password of desired length
password_length = 12  # you can change this length
password = [random.choice(all_chars) for _ in range(password_length)]

# Shuffle the password to make it more random
random.shuffle(password)

# Convert list to string
final_password = ''.join(password)

print("Generated Password:", final_password)
