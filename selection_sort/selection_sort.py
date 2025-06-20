def selection_sort(arr):
    for i in range(len(arr)-1):
        index = i
        print(index)
        for x in range(i+1, len(arr)):
            if arr[x]<arr[i]:
                index = x
        minval = arr.pop(index)
        arr.insert(i, minval)
    return arr


