#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:

#1.Open brackets must be closed by the same type of brackets.
#2.Open brackets must be closed in the correct order.
#3.Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs:
               if not stack or stack.pop() != pairs[ch]:
                  return False
            else:
                stack.append(ch)
        return not stack