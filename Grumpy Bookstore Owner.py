#There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.
#During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.
#The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.
#Return the maximum number of customers that can be satisfied throughout the day.

class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        n = len(customers)

        # Customers already satisfied
        satisfied = 0

        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]

        # First window: extra customers we can satisfy
        extra = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]

        max_extra = extra

        # Sliding window
        for i in range(minutes, n):

            # Add new customer entering the window
            if grumpy[i] == 1:
                extra += customers[i]

            # Remove customer leaving the window
            if grumpy[i - minutes] == 1:
                extra -= customers[i - minutes]

            max_extra = max(max_extra, extra)

        return satisfied + max_extra