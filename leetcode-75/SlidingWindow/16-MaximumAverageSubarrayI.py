# 643. Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000
 

# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104

def max_avg_salary(nums, k):

    currsum = 0
    maxsum = 0

    i = 0
    j = k
    l = len(nums)

    currsum = sum(nums[:k])
    maxsum = currsum

    while j<l:

        currsum = currsum - nums[i] + nums[j]
        maxsum = max(currsum, maxsum)

        i += 1
        j += 1

    return maxsum/k

def main():

    numslist = list(map(int, input("Enter list of numbers: ").split()))
    kvalue = int(input("Enter k value: "))
    result = max_avg_salary(numslist, kvalue)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()