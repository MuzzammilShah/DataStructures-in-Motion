# 151. Reverse Words in a String

# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

# Constraints:

# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.

#=====SOLUTION=====

def reverse_word_method1(s):

    n = len(s)
    i = 0
    words = []

    while i<n and s[i] == ' ':
        i += 1

    while i<n:

        word = []

        while i<n and s[i] != ' ':
            word.append(s[i])
            i += 1

        if word:
            words.append(''.join(word))

        while i<n and s[i] == ' ':
            i += 1

    return ' '.join(words[::-1]) #We reverse them here

def reverse_word_method2(s):

    formatted = (s.strip()).split()
    formatted.reverse()

    return ' '.join(formatted)

def main():

    input_string = input("Enter sentence: ")
    output1 = reverse_word_method1(input_string)
    output2 = reverse_word_method2(input_string)
    print(f"Method1: {output1}")
    print(f"Method2: {output2}")

if __name__ == "__main__":
    main()