def wave(arr):
    l=0
    r=len(arr)-1
    c=0
    ans=-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid-1]<arr[mid]<arr[mid+1]:
            ans= arr[mid]
        elif arr[mid]>arr[mid-1]:
            l=mid+1
        elif arr[mid]<arr[mid-1]:
            r=mid-1
    return ans
arr=[1,3,4,5,9,6,2,-1]
ans=wave(arr)
print(ans)
# def find_max_in_bitonic(arr):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2

#         # Check if mid is the peak
#         if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] > arr[mid + 1]):
#             return arr[mid]

#         # If the sequence is still increasing, move right
#         if arr[mid] > arr[mid - 1]:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1  # Should never reach here

# # Example usage
# arr = [1, 3, 4, 5, 9, 6, 2, -1]
# print(find_max_in_bitonic(arr))  # Output: 9
