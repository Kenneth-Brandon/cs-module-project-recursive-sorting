# TO-DO: Implement a recursive implementation of binary search

# Compare x with the middle element.
# If x matches with the middle element, we return the mid index.
# Else if x is greater than the mid element, then x can only lie in the right(greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
# Else if x is smaller, the target x must lie in the left(lower) half. So we apply the algorithm for the left half.

import math


def binary_search(arr, target, start, end):
    # Your code here
    if len(arr) == 0:
        return -1
    mid = math.floor((start + end)/2)
    if arr[mid] == target:
        return mid
    elif start >= end:
        return -1
    else:
        if target > arr[mid]:
            return binary_search(arr, target, mid + 1, end)
        else:
            return binary_search(arr, target, start, mid - 1)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target, start=0, end=None):
    # Your code here
    if len(arr) == 0:
        return -1
    if end == None:
        end = len(arr) - 1
    # dir = -1 if array is descending, 1 if ascending
    dir = -1 if arr[0] > arr[-1] else 1
    mid = math.floor((start + end)/2)
    if arr[mid] == target:
        return mid
    elif start >= end:
        return -1
    else:
        if dir * target > dir * arr[mid]:
            return agnostic_binary_search(arr, target, mid + 1, end)
        else:
            return agnostic_binary_search(arr, target, start, mid - 1)


# A good example of a program that is data agnostic is one which retrieves, updates, sorts, and / or writes, data using SQL statements. The program neither knows nor cares how underlying files holding the data are organized, and , depending on whether an SQL interface module (compatibility layer) to handle differences between different database systems was employed, might be completely unaware what database system was being used.
