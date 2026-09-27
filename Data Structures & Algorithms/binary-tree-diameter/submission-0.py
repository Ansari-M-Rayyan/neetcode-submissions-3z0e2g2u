# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Left aur right subtree ki height nikalo
            left_height = get_height(node.left)
            right_height = get_height(node.right)

            # Agar ye node highest/turning point ho, toh path edges = left + right
            # Global diameter ko update karo
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Parent ko apni actual height return karo
            return 1 + max(left_height, right_height)

        get_height(root)
        return self.max_diameter

# Use postorder recursion to calculate the height of each subtree.
# At every node, the longest path passing through it is left height + right height.
# Track the maximum such path as the tree's diameter, while returning the
# node's height to its parent.
# Time: O(n), Space: O(h) where h is the tree height.