def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1 
    right = 2 * i + 2
    
    if left < n and arr[i] < arr[left]:
        largest = left
    
    if right < n and arr[i] < arr[right]:
        largest = right
        
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)



def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((len(array)//2)-1, -1, -1):
            heapify(array, size, i)
        
arr = []

insert(arr,3)

insert(arr,4)
insert(arr,9)
insert(arr,10)
insert(arr,5)
insert(arr,2)


print("Max_Heap array: " + str(arr))
