#You are given an integer array nums consisting of n elements, and an integer k.
#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution(object):

    def findMaxAverage(self, nums, k):
        # Sum of the first window
        window_sum = sum(nums[:k])

        # Initially, first window has the maximum sum
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]

            if window_sum > max_sum:
                max_sum = window_sum

        return float(max_sum) / k