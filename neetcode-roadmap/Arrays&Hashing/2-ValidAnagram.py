# 242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 
# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# ---------

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # sList = list(s)
        # tList = list(t)

        sHash = defaultdict(int)
        tHash = defaultdict(int)

        for i in s:
            sHash[i] += 1

        for j in t:
            tHash[j] += 1

        if sHash == tHash:
            return True
        else:
            return False