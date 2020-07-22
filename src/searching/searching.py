# from pudb import set_trace as st

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    mid = (start + end) // 2
    # st()
    if end < start:
        return -1
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid, end)
    else:
        return binary_search(arr, target, start, mid)
    # return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively


# def agnostic_binary_search(arr, target):
#     # st()
#     if len(arr) == 0:
#         return -1
    
#     mid = len(arr) // 2

#     if arr[mid] == target:
#         return mid

#     first_half = agnostic_binary_search(arr[:mid], target)
#     second_half = agnostic_binary_search(arr[mid+1:], target)
#     if first_half != -1:
#         return first_half

#     if second_half != -1:
#         return second_half

#     return -1