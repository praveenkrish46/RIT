def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = []
n = int(input("Enter the number of elements: "))                

print("Enter the elements one by one:")
for _ in range(n):
    num = int(input())
    arr.append(num)

key = int(input("Enter the key element to search: "))

result = linear_search(arr, key)                                
                                                                
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
