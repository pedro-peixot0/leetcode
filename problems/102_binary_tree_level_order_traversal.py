from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        all_level_order = [[root.val]]

        level = [root.left, root.right]
        while level:
            next_level = []
            level_order = []

            for node in level:
                if node is None:
                    continue

                level_order.append(node.val)

                next_level.append(node.left)
                next_level.append(node.right)

            level = next_level
            if level_order:
                all_level_order.append(level_order)

        return all_level_order
