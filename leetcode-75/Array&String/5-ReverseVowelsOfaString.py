# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"


# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

#=====SOLUTION=====

def reverse_str(s):

    vowels = ['a', 'e', 'i', 'o', 'u']

    total = len(s)
    list_s = list(s)
    left = 0
    right = total-1

    while right >= left:

        if list_s[left].lower() in vowels:

            if list_s[right].lower() in vowels:

                temp = list_s[left]
                list_s[left] = list_s[right]
                list_s[right] = temp

                left += 1
                right -= 1

            else:
                right -= 1
        
        else:
            left += 1

    return ''.join(list_s)

def main():

    string = input("Enter a string: ")
    print("Reversed:", reverse_str(string))


if __name__ == "__main__":
    main()