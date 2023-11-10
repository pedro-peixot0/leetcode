from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def _list_to_list_node(list_to_transform:list):
        if not list_to_transform:
            return None

        list_to_transform.reverse()
        
        list_node = ListNode(val=list_to_transform[0],next=None)
        for i in list_to_transform[1:]:
            list_node = ListNode(val=i,next=list_node)
        
        return list_node

    @staticmethod
    def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        all_values = []
        while True:
            if not lists:
                break
            list_node = lists.pop(0)

            while True:
                if list_node is None:
                    break
                all_values.append(list_node.val)
                list_node = list_node.next

        return Solution._list_to_list_node(sorted(all_values))
