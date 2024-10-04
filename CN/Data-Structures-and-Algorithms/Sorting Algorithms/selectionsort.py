def sel_sort(arr):
    n = len(arr)
    
    for i in range(n):  
        min_index = i                                          
        for j in range(i+1, n):                                
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]        

arr = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input())  
    arr.append(element)
sel_sort(arr)                                            
print("Sorted array:", arr)
