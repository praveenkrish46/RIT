def qs(arr):
    if len(arr) <= 1:
        return arr 
    
    pivot = arr[len(arr) // 2]                           
    left = [x for x in arr if x < pivot]                 
    middle = [x for x in arr if x == pivot]              
    right = [x for x in arr if x > pivot]                
    return qs(left) + middle + qs(right) 

arr = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input())  
    arr.append(element)

sorted_arr = qs(arr)                              
print("Sorted array:", sorted_arr)
