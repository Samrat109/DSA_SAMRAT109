#Given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right, and return the reversed list.

class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        prev = None
        current = head

        for i in range(left - 1):
            prev = current
            current = current.next

        connection = prev
        tail = current

        for i in range(right - left + 1):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        if connection:
            connection.next = prev
        else:
            head = prev

        tail.next = current

        return head