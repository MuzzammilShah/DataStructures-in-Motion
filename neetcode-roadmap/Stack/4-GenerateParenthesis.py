# 22. Generate Parentheses
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        result = []

        def recursive(open, closed):

            if open==closed==n:
                result.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                recursive(open+1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                recursive(open, closed+1)
                stack.pop()

        recursive(0, 0)
        return result