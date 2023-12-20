from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(0)

        cur_node = start
        rest = 0
        while l1 or l2 or rest > 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            add = l1_val + l2_val + rest
            rest = add // 10

            cur_node.next = ListNode(add % 10)

            cur_node = cur_node.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return start.next
