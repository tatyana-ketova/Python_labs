"""
1. Given a list of integers, return True if the sequence of numbers 1, 2, 3
 appears in the list somewhere.

Example:

arrayCheck([1, 1, 2, 3, 1]) → True
arrayCheck([1, 1, 2, 4, 1]) → False
arrayCheck([1, 1, 2, 1, 2, 3]) → True
"""

def find123(n_list):
    n=False
    for i in range(len(n_list)-1):
        if (n_list[i]==1) and (n_list[i+1]==2) and (n_list[i+2]==3):
            n = True
    return n

array1 = [1, 1, 2, 3, 1]
array2 = [1, 1, 2, 4, 1]
array3 = [1, 1, 2, 1, 2, 3]

print(find123(array1))
print(find123(array2))
print(find123(array3))



