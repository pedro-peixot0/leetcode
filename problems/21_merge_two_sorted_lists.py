from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def get_smallest() -> int:
            nonlocal list1, list2
            if list1:
                if list2:
                    if list1.val <= list2.val:
                        temp_val = list1.val
                        list1 = list1.next
                        return temp_val
                    else: 
                        temp_val = list2.val
                        list2 = list2.next
                        return temp_val
                else:
                    temp_val = list1.val
                    list1 = list1.next
                    return temp_val
            elif list2:
                temp_val = list2.val
                list2 = list2.next
                return temp_val

            return None

        starting_val = get_smallest()

        if starting_val is None:
            return None

        new_list = ListNode(val=starting_val)
        last_node = new_list

        while True:
            min_val = get_smallest()
            if min_val is None:
                break

            last_node.next = last_node = ListNode(val=min_val)

        return new_list
