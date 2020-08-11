# TO-DO: Implement a recursive implementation of binary search
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
