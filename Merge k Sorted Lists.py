#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]

                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                merged.append(self.mergeTwoLists(l1, l2))

            lists = merged

        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next