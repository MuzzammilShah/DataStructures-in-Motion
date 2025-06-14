# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

#=====SOLUTION=====

def prod_except_i(nums):

    n = len(nums)
    final = []

    prefix = [1] * n
    suffix = [1] * n

    for i in range(1,n):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    for i in range(n):
        final.append(prefix[i] * suffix[i])

    return final

def main():

    array_nums = list(map(int, input("Enter array/list of values: ").split()))
    result = prod_except_i(array_nums)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()


# NOTE
# ❌ No division allowed.
# So you can’t do:

# ```
# total_product = product(nums)
# answer[i] = total_product // nums[i]
# ```
# Instead, the trick is to use prefix and suffix products.