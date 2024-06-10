# Python program of above implementation
def getMinMax(LOW, high, arr):
    arr_max = arr[LOW]
    arr_min = arr[LOW]

    
    if LOW == high:
        arr_max = arr[LOW]
        arr_min = arr[LOW]
        return (arr_max, arr_min)

    # If there is only two element
    elif high == LOW + 1:
        if arr[LOW] > arr[high]:
            arr_max = arr[LOW]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[LOW]
        return (arr_max, arr_min)
    else:

        # If there are more than 2 elements
        mid = int((LOW + high) / 2)
        arr_max1, arr_min1 = getMinMax(LOW, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)

    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))


# Driver code
arr = [1000, 11, 445, 48, 330, 3000]
arr_max, arr_min = getMinMax(LOW, high, arr)
print('Minimum element is ', arr_min)
print('Maximum element is ', arr_max)
