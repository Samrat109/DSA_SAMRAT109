#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class Solution(object):
    def isSameTree(self, p, q):

        if p is None and q is None:
           return True

        if p is None or q is None:
           return False

        if p.val != q.val:
           return False
         
        first= self.isSameTree(p.left, q.left)
        second= self.isSameTree(p.right, q.right)

        return first and second