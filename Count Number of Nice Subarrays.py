#Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
#Return the number of nice sub-arrays.

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            """Count subarrays with at most k odd numbers"""
            if k < 0:
                return 0
            
            left = 0
            count = 0
            odd_count = 0
            
            for right in range(len(nums)):
                # Add current element if it's odd
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                # Shrink window if we have too many odd numbers
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                # All subarrays ending at 'right' with at most k odds
                count += right - left + 1
            
            return count
        
        return atMost(k) - atMost(k - 1)