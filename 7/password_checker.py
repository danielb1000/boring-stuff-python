"""
Write a function that uses regular expressions to make sure the password string it is passed is strong.
A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.
You may need to test the string against multiple regex patterns to validate its strength
"""

import re

# not using compiled regex
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


# using compiled regular expressions
pattern_length = re.compile(r'.{8,100}')
pattern_lowercase = re.compile(r'[a-z]')
pattern_uppercase = re.compile(r'[A-Z]')
pattern_digit = re.compile(r'\d')

def is_strong_password_compiled(password: str) -> bool:
    # 8 chars
    if not pattern_length.search(password):
        return False
    
    # 1 <= lowercase
    if not pattern_lowercase.search(password):
        return False

    # 1 <= uppercase
    if not pattern_uppercase.search(password):
        return False

    # 1 <= digit
    if not pattern_digit.search(password):
        return False

    return True

print(is_strong_password("tomorrow"))
print(is_strong_password("tomorrow1"))
print(is_strong_password("Tomorrow"))
print(is_strong_password("Tomorrow1"))
print()
print(is_strong_password_compiled("tomorrow"))
print(is_strong_password_compiled("tomorrow1"))
print(is_strong_password_compiled("Tomorrow"))
print(is_strong_password_compiled("Tomorrow1"))