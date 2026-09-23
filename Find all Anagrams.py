#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window_count = [0] * 26

        # Count characters in p
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        left = 0
        result = []

        for right in range(len(s)):

            # Add current character
            window_count[ord(s[right]) - ord('a')] += 1

            # Keep window size equal to len(p)
            if right - left + 1 > len(p):
                window_count[ord(s[left]) - ord('a')] -= 1
                left += 1

            # Check whether current window is an anagram
            if window_count == p_count:
                result.append(left)

        return result