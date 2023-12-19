# time complexity: O(n)
# space complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for _ in range(n):
            fast = fast.next

        # if fast has reached the end
        # it means that n == len(head)
        if fast is None:
            # so we just need to remove the first node
            return head.next

        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next

        # delete nth node
        slow.next = slow.next.next

        return head
