#Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

#Return the minimized largest sum of the split.

#A subarray is a contiguous part of the array.


class Solution(object):
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num <= mid:
                    current_sum += num
                else:
                    subarrays += 1
                    current_sum = num

            if subarrays <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left