def selection_sort(arr):
    for i in range(len(arr)-1):
        index = i
        print(index)
        for x in range(i+1, len(arr)):
            if arr[x]<arr[index]:
                index = x
        arr[i], arr[index] = arr[index], arr[i]
    return arr
