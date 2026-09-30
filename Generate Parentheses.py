#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution(object):

    def generateParenthesis(self, n):

        result = []
        stack = []

        def backtrack(open_count, close_count):

            # Complete valid combination
            if open_count == n and close_count == n:
                result.append("".join(stack))
                return

            # Add '('
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()

            # Add ')'
            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()

        backtrack(0, 0)

        return result