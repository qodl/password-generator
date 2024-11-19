import random
import string

def create_password(length):
    """
    Generates a random password of the specified length.
    Ensures the password includes at least one letter, one digit, and one symbol.
    
    Parameters:
    length (int): The length of the password (must be at least 6).
    
    Returns:
    str: The generated password.
    """
    if length < 6:
        raise ValueError("Password length must be at least 6.")

    # Define possible characters
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # Special characters like !, @, #

    # Combine all character sets
    all_characters = letters + digits + symbols

    # Ensure the password has at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 3)

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    while True:
        try:
            # Ask the user for password length
            user_length = int(input("Enter the desired password length (minimum 6): "))
            
            # Generate and display the password
            generated_password = create_password(user_length)
            print(f"Your generated password is: {generated_password}")
            break  # Exit the loop
        except ValueError as e:
            print(e)

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()

