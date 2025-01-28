# 283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1

#=====SOLUTION=====

def move_zeroes(nums):

    write, read = 0, 0

    while read < len(nums):

        if nums[read] != 0:

            nums[write], nums[read] = nums[read], nums[write]
            write += 1

        read += 1

    return nums

def main():

    input_list = list(map(int, input("Enter list of numbers: ").split()))
    output = move_zeroes(input_list)
    print(f"Output: {output}")


if __name__ == "__main__":
    main()