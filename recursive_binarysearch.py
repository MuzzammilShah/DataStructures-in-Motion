array = [10]

def main():
    length = len(array)
    l=0
    h=length-1
    key = int(input("Enter key to be searched: "))
    output = RBinSearch(l, h, key)
    print(output)


def RBinSearch(low, high, key):

    #If there is only one element present in the array
    if(low==high):
        if(array[low] == key):
            return f"element found in: {low}"
        else:
            return "element not present"
        
    else:

        if low > high:
            return "element not present"

        mid = (low+high) // 2

        if(array[mid] == key):
            return f"element found in: {mid}"
        
        if(array[mid] > key):
            return RBinSearch(low, mid-1, key)
        else:
            return RBinSearch(mid+1, high, key)

        
if __name__ == "__main__":
    main()