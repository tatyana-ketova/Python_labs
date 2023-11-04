"""
2. Given a string, return a new string made of every other character starting
with the first, so "Hello" yields "Hlo".

Example:

stringBits('Hello') → 'Hlo'
stringBits('Hi') → 'H'
stringBits('Heeololeo') → 'Hello'
"""

def changeStr(string):
    n = list(string)
    new_list = n[::2]
    new_str=""
    new_str=new_str.join(new_list)
    return new_str



print(changeStr('Hello'))
print(changeStr('Hi'))
print(changeStr('Heeololeo'))