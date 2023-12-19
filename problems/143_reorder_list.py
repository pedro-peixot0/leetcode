from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        references = []
        while head:
            references.append(head)
            head = head.next

        len_ref = len(references)
        mid = len_ref // 2
        for cur in range(mid):
            target = len_ref - cur - 1
            references[cur].next = references[target]
            references[target].next = references[cur + 1]

        references[mid].next = None
