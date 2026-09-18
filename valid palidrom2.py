#Given a string s, return true if the s can be palindrome after deleting at most one character from it.

class Solution(object):

    def isPalindrome(self, s, l, r):

        while l < r:

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True


    def validPalindrome(self, s):

        l = 0
        r = len(s) - 1

        while l < r:

            if s[l] != s[r]:

                #Delete left character
                if self.isPalindrome(s, l + 1, r):
                    return True

                # Delete right character
                if self.isPalindrome(s, l, r - 1):
                    return True
                return False

            l += 1
            r -= 1

        return True