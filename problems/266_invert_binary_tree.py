from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive_inverter(node):
            if not node:
                return

            node.right, node.left = recursive_inverter(node.left), recursive_inverter(node.right)

            return node

        return recursive_inverter(root)
