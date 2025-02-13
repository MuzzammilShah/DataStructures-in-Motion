# 1207. Unique Number of Occurrences

# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# Example 1:

# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: arr = [1,2]
# Output: false
# Example 3:

# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
 

# Constraints:

# 1 <= arr.length <= 1000
# -1000 <= arr[i] <= 1000

#=====SOLUTION=====

from collections import defaultdict

def unique_num(nums):

    hashtable = defaultdict(int)

    for num in nums:
        hashtable[num] += 1

    settable = set(hashtable.values())

    return len(hashtable.values()) == len(settable)


def main():

    inputnums = list(map(int, input("Enter list value: ").split()))
    result = unique_num(inputnums)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()