def insertion_sort(array):
    n = len(array)
    
    for i in range(1, n):
        key = array[i]                                 
        j = i - 1
        
        while j >= 0 and array[j] > key:               
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key                             

array = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input()) 
    array.append(element)

insertion_sort(array)                                  
print("Sorted array:", array)
