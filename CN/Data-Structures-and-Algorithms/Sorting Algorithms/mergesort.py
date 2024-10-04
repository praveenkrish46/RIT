def mers(arr):
    if len(arr) <= 1:
        return arr 

    mid = len(arr) // 2                            
    left = mers(arr[:mid])
    right = mers(arr[mid:])
    return merge(left, right)                       

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):         
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])                        
    result.extend(right[j:])
    return result
arr = []
n = int(input("Enter number of elements: ")) 

print("Enter the elements:")
for i in range(n):
    element = int(input()) 
    arr.append(element)

sorted_arr = mers(arr)                         
print("Sorted array:", sorted_arr)
