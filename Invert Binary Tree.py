#Given the root of a binary tree, invert the tree, and return its root.

class Solution(object):
    def invertTree(self, root):

        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root