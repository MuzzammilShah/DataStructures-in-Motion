# 1679. Max Number of K-Sum Pairs

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

# ==== SOLUTION =====

from collections import defaultdict

def hashmap_one(nums, k):

    hashtable = defaultdict(int)
    operations = 0

    for num in nums:

        complement = k - num

        if hashtable[complement] > 0:

            hashtable[complement] -= 1
            operations += 1

        else:

            hashtable[num] += 1

    return operations


def main():

    inputnums = list(map(int, input("Enter list of numbers: ").split()))
    inputk = int(input("Enter value of k: "))
    result = hashmap_one(inputnums, inputk)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()