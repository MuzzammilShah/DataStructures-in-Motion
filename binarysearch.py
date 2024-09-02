sortedarray = [9, 12, 17, 23, 25, 31, 33, 42, 49]
arraylength = len(sortedarray)
low = 0
high = arraylength - 1

key = int(input("Enter Key to be found"))
found = False

while(low <= high):

    mid = (low+high) // 2   #To ensure that the floor value is considered

    if sortedarray[mid] == key:
        print("Key found in position: ",mid)
        found=True
        break
    
    elif sortedarray[mid] < key:
        low = mid+1

    else:
        high = mid-1

if not found:
    print("Key doesnot exist in array")