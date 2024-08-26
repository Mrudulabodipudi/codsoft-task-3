import random
import string

def generate_strong_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 for strong passwords")
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Ensure at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    remaining_length = length - 4
    all_characters = lower + upper + digits + punctuation
    password += random.choices(all_characters, k=remaining_length)
    
    # Shuffle the result to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

# Example usage
password_length = 12
password = generate_strong_password(password_length)
print("Generated strong password:", password)
