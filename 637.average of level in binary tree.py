#Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
# Answers within 10-5 of the actual answer will be accepted.

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):

        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            size = len(queue)
            total = 0

            for i in range(size):
                node = queue.popleft()

                total += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(total / float(size))

        return result