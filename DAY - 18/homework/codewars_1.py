def find_smallest_int(arr):   #make function name: find_smallest_int
    x = 0                 # x is variable which is equal to 0
    for i in arr:             #  i am using for loop to check all item
        if i < i + 1 :
            x = i
            i += 1
    return x

print(find_smallest_int([44,104,234,1,56,-44]))


# or this code is working also
# return min(arr)