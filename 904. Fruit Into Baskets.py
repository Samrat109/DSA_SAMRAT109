#You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
#You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
#Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
#Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
#Given the integer array fruits, return the maximum number of fruits you can pick.

class Solution(object):

    def totalFruit(self, fruits):
        left = 0
        max_fruits = 0
        count = {}

        for right in range(len(fruits)):

            # Add current fruit
            fruit = fruits[right]

            if fruit not in count:
                count[fruit] = 0

            count[fruit] += 1

            # More than 2 fruit types
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1

                if count[left_fruit] == 0:
                    del count[left_fruit]

                left += 1

            # Current window is valid
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits