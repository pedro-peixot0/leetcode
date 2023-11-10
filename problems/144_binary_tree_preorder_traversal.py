from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def preorderTraversal(root: Optional[TreeNode]) -> list[int]:

        def get_ordered(root):
            if root is None:
                return []

            left = get_ordered(root.left) 
            right = get_ordered(root.right)
            
            return left + [root.val] + right
     
        return get_ordered(root)

class Solution2:
    @staticmethod
    def preorderTraversal(root: Optional[TreeNode]) -> list[int]:
        ordered = []
        def get_ordered(root):
            nonlocal ordered
            if root is not None:
                ordered.append(root.val)

                get_ordered(root.left) 
                get_ordered(root.right)
        
        get_ordered(root)
        return ordered