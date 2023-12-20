from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hashmap = {id(None): None}

        cur = head
        while cur:
            copy = Node(cur.val)
            hashmap[id(cur)] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = hashmap[id(cur)]
            copy.next = hashmap[id(cur.next)]
            copy.random = hashmap[id(cur.random)]

            cur = cur.next

        return hashmap[id(head)]
