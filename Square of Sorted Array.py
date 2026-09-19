#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution(object):

    def sortedSquares(self, nums):

        left = 0
        right = len(nums) - 1

        result = [0] * len(nums)

        position = len(nums) - 1

        while left <= right:

            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1

            position -= 1

        return result