def binary_search(arr, val, start, end):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    # this occurs if we are moving beyond left's boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start

    mid = int((start+end)/2)
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid


print("Sorted array:")
arr = [0, 12, 17, 23, 31, 37, 46, 54, 72, 88, 100]
val = 29
j = binary_search(arr, val, 0, len(arr)-1)
print(arr)
print(j)
