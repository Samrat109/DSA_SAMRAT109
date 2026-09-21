#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.In other words, return true if one of s1's permutations is the substring of s2.

class Solution(object):

    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):

            count2[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > len(s1):
                count2[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if count1 == count2:
                return True

        return False