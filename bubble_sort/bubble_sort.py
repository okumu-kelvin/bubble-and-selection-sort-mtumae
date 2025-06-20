def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list)-1):
        for x in range(len(unsorted_list)-i-1):
            if unsorted_list[x]>unsorted_list[x+1]:
                print(f"swapping {arr[x]} with {arr[x+1]}")
                unsorted_list[x], unsorted_list[x+1]=unsorted_list[x+1], unsorted_list[x]
    return unsorted_list
    





    
   