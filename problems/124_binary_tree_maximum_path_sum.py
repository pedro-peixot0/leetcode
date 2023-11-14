from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def maxPathSum(root: Optional[TreeNode]) -> int:
        # this path sum value is the sum of the path to 2 roots
        max_sum_path = float('-inf')

        def recursive(tree_node):
            nonlocal max_sum_path
            
            if tree_node is None:
                return 0
            
            # we are using the max here because we can choose to ignore a root
            left_result = max(recursive(tree_node.left), 0)
            right_result = max(recursive(tree_node.right), 0)

            # if we select both sides of the tree this is a complete path. (2 roots)
            whole_path_this_node = tree_node.val + left_result + right_result
            if whole_path_this_node > max_sum_path:
                max_sum_path = whole_path_this_node
            
            # only select one of the roots to return to the node above
            return max(left_result, right_result) + tree_node.val
            
        recursive(root)
        return max_sum_path
            
        