#Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque

class Solution(object):
    def levelOrder(self, root):

        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:

            level_size = len(queue)
            current_level = []

            for i in range(level_size):

                node = queue.popleft()

                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result