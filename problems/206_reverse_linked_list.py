from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# iterative solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        while head:
            new_list = ListNode(
                val=head.val, 
                next=new_list
            )
            head = head.next

        return new_list

# recursive solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        def recursive_inversion(next_node) -> None:
            nonlocal new_list

            if not next_node:
                return None

            new_list = ListNode(
                val=next_node.val,
                next=new_list
            )

            return recursive_inversion(next_node.next)

        recursive_inversion(head)
        return new_list
