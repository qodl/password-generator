# Password Generator

A Python script to generate secure random passwords. This script ensures that passwords include a mix of uppercase letters, lowercase letters, numbers, and special characters. It can be used as both a standalone program and an importable module for integration into other Python projects.

---

## Features

- Generates strong passwords with a specified length.
- Ensures at least one letter, one digit, and one special character in the password.
- Includes validation to enforce a minimum password length of 6.
- Can be integrated into other Python projects as a reusable module.

---

## Installation

There are no external dependencies required for this project. It uses only Python’s built-in libraries.

---

## Usage

### Standalone Script

Run the script directly in your terminal:

```bash
python password_generator.py

```
### Importing as a Module
You can use the password generation function in other Python scripts by importing it:

Save the script as password_generator.py.

Import the create_password function into your project:

```bash
from password_generator import create_password

# Call the create_password() function with the desired length:
print("Your generated password is:", create_password(9))
```


### Parameters:
**length (int):** The desired length of the password. Must be 6 or greater.
### Returns:
**str:** A randomly generated password.
### Raises:
**ValueError:** If the provided length is less than 6.
### Requirements
This script uses Python’s built-in libraries:

**random**

**string**
