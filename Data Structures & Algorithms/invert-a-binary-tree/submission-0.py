# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        # swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        # recursion call
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Recursively invert the binary tree by swapping the left and right children
# of every node, then recursively inverting both subtrees.
# Time: O(n), Space: O(h) where h is the tree height.