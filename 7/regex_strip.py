"""
Regex Version of the strip() Method
Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.
"""

import re

def regex_strip(string: str, chars_to_remove: str = None) -> str:
    # whitespaces
    pattern = r'^\s+|\s+$'
    if chars_to_remove is not None:
        escaped_chars = re.escape(chars_to_remove)

        # this pattern removes whitespaces along with the provided chars_to_remove
        pattern = f'^[\s{escaped_chars}]+|[\s{escaped_chars}]+$'

    return re.sub(pattern, '', string)


print(regex_strip("   Hello, World!   "))  
print(regex_strip("  xx99999999Hello, World!xxy", "y9x"))  

