# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# =====SOLUTION=====

def container_water(nums):

    left = 0
    right = len(nums)-1

    maxarea = 0

    while right >= left:

        checkarea = (right - left) * min(nums[right], nums[left])

        if checkarea > maxarea:
            maxarea = checkarea

        if nums[right] < nums[left]:
            right -= 1

        else:
            left += 1

    return maxarea


def main():

    nums = list(map(int, input("Enter list of numbers: ").split()))
    result = container_water(nums)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()