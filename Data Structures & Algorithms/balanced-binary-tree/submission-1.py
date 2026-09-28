# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def heigh(node):
            if not node:
                return 0

            left_h = heigh(node.left)
            right_h = heigh(node.right)

            if left_h is False or right_h is False:
                return False
            
            diff = abs(left_h - right_h)

            if diff > 1:
                return False

            return 1 + max(left_h, right_h)

        return heigh(root) is not False

# Recursively calculate the height of each subtree and check whether the height
# difference between the left and right subtrees is at most 1.
# Return False immediately if any subtree is unbalanced; otherwise return its
# height and finally check whether the whole tree is balanced.
# Time: O(n), Space: O(h) where h is the tree height.
        