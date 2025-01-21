# 1071. Greatest Common Divisor of Strings

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

#=====SOLUTION=====

import math

def check_gcd(str1, str2):

    gcd = math.gcd(len(str1), len(str2))

    gcd_str = str1[:gcd]

    if ( (gcd_str * (len(str1) // len(gcd_str)) == str1) and (gcd_str * (len(str2) // len(gcd_str)) == str2) ):
        return gcd_str
    else:
        return ""
    
def main():

    input1 = input("Enter first string: ")
    input2 = input("Enter second string: ")
    output = check_gcd(input1, input2)
    print(f"Result: {output}")

if __name__ == "__main__":
    main()