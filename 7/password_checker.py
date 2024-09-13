"""
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength
"""

import re

def is_strong_password(password: str) -> bool:
    # 8 chars
    if not re.search(r'.{8,100}', password):
        return False
    
    # 1 <= lowercase
    if not re.search(r'[a-z]', password):
        return False

    # 1 <= uppercase
    if not re.search(r'[A-Z]', password):
        return False

    # 1 <= digit
    if not re.search(r'\d', password):
        return False

    return True

print(is_strong_password("tomorrow"))
print(is_strong_password("tomorrow1"))
print(is_strong_password("Tomorrow"))
print(is_strong_password("Tomorrow1"))