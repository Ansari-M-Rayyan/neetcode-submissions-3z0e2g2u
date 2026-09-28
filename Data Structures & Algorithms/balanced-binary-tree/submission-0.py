# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Left subtree ki height nikalo
            left = check_height(node.left)
            if left == -1:
                return -1  # Left subtree already unbalanced hai
            
            # Right subtree ki height nikalo
            right = check_height(node.right)
            if right == -1:
                return -1  # Right subtree already unbalanced hai
            
            # Current node par balance check
            if abs(left - right) > 1:
                return -1  # Current node unbalanced hai
            
            # Agar balanced hai, normal height return karo
            return 1 + max(left, right)

        return check_height(root) != -1

# Use postorder recursion to calculate subtree heights while checking balance at
# every node. Return -1 immediately if any subtree is unbalanced, otherwise
# return the current subtree's height.
# Time: O(n), Space: O(h) where h is the tree height.
