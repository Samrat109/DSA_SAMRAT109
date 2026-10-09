#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.

#You must not use any built-in exponent function or operator.

    #For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x

        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                left = mid + 1

            else:
                right = mid - 1

        return right