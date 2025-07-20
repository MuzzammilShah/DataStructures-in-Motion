# 1004. Max Consecutive Ones III

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

def max_consecutive(nums, k):

    left = 0
    count_zeroes = 0
    max_length = 0

    for right in range(len(nums)):

        if nums[right] == 0:
            count_zeroes += 1

        while count_zeroes > k:

            if nums[left] == 0:
                count_zeroes -= 1
            
            left += 1

        max_length = max(max_length, right-left+1)

    return max_length

def main():

    inplist = list(map(int, input("Enter list of binary values: ").split()))
    kvalue = int(input("Enter value of k: "))
    result = max_consecutive(inplist, kvalue)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()