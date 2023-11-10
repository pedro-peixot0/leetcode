from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        all_depths = []

        def count_depth(root: TreeNode, depth: int) -> None:
            if root is None:
                all_depths.append(depth)
                return None

            depth += 1

            count_depth(root.left, depth)
            count_depth(root.right, depth)

            return None

        count_depth(root=root, depth=0)

        return max(all_depths)
