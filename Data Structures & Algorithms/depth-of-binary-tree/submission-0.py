# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Base case: empty tree has depth 0
        if not root:
            return 0
        
        # Left aur Right subtree ka depth recursively nikalo
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Maximum leke 1 + (current node ke liye) karo
        return 1 + max(left_depth, right_depth)

# Recursively calculate the depth of the left and right subtrees and take the
# larger one, adding 1 for the current node. An empty tree has depth 0.
# Time: O(n), Space: O(h) where h is the tree height.