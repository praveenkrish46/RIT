def bubble_sort(array):
    n = len(array)
    
    for i in range(n):
        swap = False                                         
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                swap = True
                array[j], array[j + 1] = array[j + 1], array[j]         
        if not swap:
            break
array = []
n = int(input("Enter number of elements: "))  

print("Enter the elements:")
for i in range(n):
    element = int(input())  
    array.append(element)

bubble_sort(array)                                               
print("Sorted array:", array)
