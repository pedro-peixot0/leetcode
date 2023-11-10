from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def _validate_tree(
        root: Optional[TreeNode],
        min_val: float = float('-inf'),
        max_val: float = float('inf'),
    ) -> bool:
        if root is None:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False

        left = Solution._validate_tree(root.left, min_val, root.val)
        right = Solution._validate_tree(root.right, root.val, max_val)

        return left and right

    @staticmethod
    def isValidBST(root: Optional[TreeNode]) -> bool:
        return Solution._validate_tree(root)
