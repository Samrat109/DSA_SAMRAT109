#You are given two positive integer arrays spells and potions, of length n and m respectively, 
# where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

#You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

#Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            left = 0
            right = m - 1

            while left <= right:
                mid = (left + right) // 2

                if spell * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1

            result.append(m - left)

        return result