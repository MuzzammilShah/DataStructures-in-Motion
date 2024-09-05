array = []

def main():

    global array
    user_input = input("Enter Array of elements: ")
    array = list(map(int, user_input.replace(',',' ').split()))

    length = len(array)

    key = int(input("Enter Key to be found: "))

    l = 0
    h = length-1
    
    output = checkBinarySearch(l, h, key)
    print(output)

def checkBinarySearch(low, high, key):

    if(low == high):
        if(array[low] == key):
            return f"Element found at {low}"

    while(low <= high):

        mid = (low + high) // 2

        if(array[mid] == key):
            return f"Element found at {mid}"
        
        if(array[mid] > key):
            high = mid - 1
        else:
            low = mid + 1
    
    return "Element is not present"

if __name__ == "__main__":
    main()