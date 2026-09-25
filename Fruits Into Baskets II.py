#You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.

#From left to right, place the fruits according to these rules:
#Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the quantity of that fruit type.
#Each basket can hold only one type of fruit.
#If a fruit type cannot be placed in any basket, it remains unplaced.
#Return the number of fruit types that remain unplaced after all possible allocations are made.

class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        n = len(fruits)
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            placed = False

            for j in range(n):
                if not used[j] and baskets[j] >= fruit:
                    used[j] = True
                    placed = True
                    break

            if not placed:
                unplaced += 1

        return unplaced