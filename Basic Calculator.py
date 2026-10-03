#Given a string s which represents an expression, evaluate this expression and return its value. 
#The integer division should truncate toward zero.
#You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
#Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        num = 0
        operator = '+'

        for i in range(len(s)):

            ch = s[i]

            # Build the complete number
            if ch.isdigit():
                num = num * 10 + int(ch)

            # Process operator when we find one
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:

                if operator == '+':
                    stack.append(num)

                elif operator == '-':
                    stack.append(-num)

                elif operator == '*':
                    stack[-1] = stack[-1] * num

                elif operator == '/':
                    # Truncate division toward zero
                    stack[-1] = int(stack[-1] / num)

                operator = ch
                num = 0

        return sum(stack)