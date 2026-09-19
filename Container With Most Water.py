#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
#Notice that you may not slant the container.

class Solution(object):

    def maxArea(self, height):

        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:

            width = right - left

            if height[left] < height[right]:
                h = height[left]
                left += 1
            else:
                h = height[right]
                right -= 1

            area = width * h

            if area > max_water:
                max_water = area

        return max_water