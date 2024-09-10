array = []

def main():
    global array

    user_input = input("Enter a list of array element: ")
    array = list(map(int, user_input.replace(',', ' ').split()))

    key = int(input("Enter element to be found: "))

    length = len(array)

    low = 0
    high = length-1

    result = BinarySearch(low, high, key)
    print(result)

def BinarySearch(l, h, k):

    if l == h:
        if array[l] == k:
            return f"Element found at {l}"
        return f"Element not found"
        
    while(l <= h):

        mid = (l+h) // 2

        if array[mid] == k:
            return f"Element found at {mid}"
        
        if array[mid] > k:
            h = mid - 1
        else:
            l = mid + 1

    return f"Element not found"

if __name__ == "__main__":
    main()