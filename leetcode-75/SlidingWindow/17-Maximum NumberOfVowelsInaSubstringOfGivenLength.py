# 1456. Maximum Number of Vowels in a Substring of Given Length
# Hint
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

def max_vowels(s, k):

    vowels = {'a', 'e', 'i', 'o', 'u'}
    countvowels = 0
    maxvowels = 0

    for i in range(k):
        if s[i] in vowels:
            countvowels += 1
            i += 1
    
    maxvowels = max(countvowels, maxvowels)

    for i in range(k, len(s)):

        if s[i-k] in vowels:
            countvowels -= 1
        
        if s[i] in vowels:
            countvowels += 1

        maxvowels = max(maxvowels, countvowels)
        i += 1

    return maxvowels


def main():

    inputs = input("Enter string: ")
    kvalue = int(input("Enter value of k: "))
    result = max_vowels(inputs, kvalue)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()