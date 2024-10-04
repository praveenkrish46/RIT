def binary_search(arr, key):
    if len(arr) == 0:
        return -1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid                                               
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1                                                        
                                                                     
def main():                                                                      
    size = input("Enter size of  array: ")                    
    while size == '':                                                
        print("Input cannot be empty. enter a valid number.")
        size = input("Enter size of array: ")                
    size = int(size)                                                 
    
    arr = []                                                         
    print("Enter the sorted array:")
    for i in range(size):
        element = int(input(f"Element {i + 1}: "))
        arr.append(element)
    key = int(input("Enter search element : "))

    result = binary_search(arr,key)                              
    if result != -1:
        print(f"Binary Search: key element found at index {result}")
    else:
        print("Binary Search: key element not found in the array")


if __name__ == "__main__":
    main()
