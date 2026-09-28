#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#Implement the MinStack class:

    #MinStack() initializes the stack object.
    #void push(int value) pushes the element value onto the stack.
    #void pop() removes the element on the top of the stack.
    #int top() gets the top element of the stack.
    #int getMin() retrieves the minimum element in the stack.

#You must implement a solution with O(1) time complexity for each function.

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if not self.minStack:
            self.minStack.append(value)
        else:
            self.minStack.append(min(value, self.minStack[-1]))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]