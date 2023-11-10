class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNodeIterable:
    def __init__(self, ln: ListNode):
        self.ln = ln
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.ln is None:
            return 0, False
        
        val = self.ln.val
        self.ln = self.ln.next
        
        return val, True
    
class Solution:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        l1 = ListNodeIterable(l1)
        l2 = ListNodeIterable(l2)

        linked_list = ListNode(val=None, next=None)
        last_node = linked_list
        carry = val = 0
        while True:
            n1, next_1 = next(l1)
            n2, next_2 = next(l2)

            if not any([next_1, next_2, carry]):
                break

            carry, val = divmod(n1 + n2 + carry, 10)

            if linked_list.val is None:
                linked_list.val = val
                continue

            
            last_node.next = ListNode(val=val, next=None)
            last_node = last_node.next 

        return linked_list
    
        