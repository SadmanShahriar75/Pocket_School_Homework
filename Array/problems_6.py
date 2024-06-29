# Find Max of two number 23,89 ? what is the max ?

def maxofArray():
    arr = [23,89]
    max_element = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]

    return max_element

print(maxofArray())
