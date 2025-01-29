# 392. Is Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

#=====SOLUTION=====

def is_subsequence(s, t):

    s_ptr, t_ptr = 0, 0

    if len(s) == 0:
        return True

    while t_ptr < len(t):

        if t[t_ptr] == s[s_ptr]:

            s_ptr += 1
        
        t_ptr += 1

    if s_ptr == len(s):
        return True
    else:
        return False
    

def main():

    s_input = input("Enter small string: ")
    t_input = input("Enter larger string: ")
    result= is_subsequence(s_input, t_input)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()

#=====Explaination=====

# t should keep traversing
# s should only increament if there is a match
# if the total increament value of s pointer is same as the lenght of s, then it is true

# for intial checks:
# if s is zero then it should be true
# if t is 0 and s is not zero, then it should return false