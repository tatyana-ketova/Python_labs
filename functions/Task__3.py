"""
Given a string, return a string where for every char in the original,
# there are two chars.

 doubleChar('The') → 'TThhee'
 doubleChar('AAbb') → 'AAAAbbbb'
 doubleChar('Hi-There') → 'HHii--TThheerree'
"""

def doubleChar(n):
    new_str = ""
    new_str = new_str.join([item*2 for item in list(n)])
    return new_str

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))