#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """

        p1 = headA
        p2 = headB

        while p1 is not p2:

            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next

            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next

        return p1