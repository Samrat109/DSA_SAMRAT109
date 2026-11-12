#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0

        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)



        return 1 + max(left,right)
