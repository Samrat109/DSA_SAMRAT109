#You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.
#Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

class Solution(object):

    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        total = sum(nums)
        target = total - x

        # We need to find the longest subarray
        # whose sum is exactly target.

        if target < 0:
            return -1

        if target == 0:
            return len(nums)

        left = 0
        current_sum = 0
        max_length = -1

        for right in range(len(nums)):
            current_sum += nums[right]

            # Shrink window if sum becomes too large
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1

            # Found a subarray with required sum
            if current_sum == target:
                length = right - left + 1
                max_length = max(max_length, length)

        if max_length == -1:
            return -1

        return len(nums) - max_length