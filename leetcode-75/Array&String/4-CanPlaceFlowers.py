# 605. Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

#=====SOLUTION=====

def flower_placing(flowerbed, n):

    if n==0:
        return True
    
    total = len(flowerbed)
    i = 0

    for i in range(total):

        if flowerbed[i] == 0:

            left_check = ( (i==0 or flowerbed[i-1])==0 )
            right_check = ( (i==(total-1) or flowerbed[i+1])==0 )

            if left_check and right_check:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True
            
    return False

def main():

    input1 = list(map(int, input("Enter list: ").split()))
    input2 = int(input("Enter n: "))
    output = flower_placing(input1, input2)
    print(output)

if __name__ == "__main__":
    main()