from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_values = []

        def move_from_smallest_to_biggest(node):
            if node is None:
                return None

            if node.left is not None:
                move_from_smallest_to_biggest(node.left)

            sorted_values.append(node.val)

            if node.right is not None:
                move_from_smallest_to_biggest(node.right)

            return None
        move_from_smallest_to_biggest(root)

        return sorted_values[k-1]
