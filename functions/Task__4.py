"""
Return the number of even integers in the given array/list.
Examples:
count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""

def count_evens(list_num):
    n=0
    for i in range(len(list_num)):
        if list_num[i]%2==0:
            n=n+1
    return n
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))