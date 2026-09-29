# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Case 1: Dono nodes None hain -> Match!
        if not p and not q:
            return True
        
        # Case 2: Ek None hai aur ek exist karta hai -> Structure mismatch!
        if not p or not q:
            return False
        
        # Case 3: Dono exist karte hain par values alag hain -> Value mismatch!
        if p.val != q.val:
            return False
        
        # Case 4: Current node match ho gaya, ab left aur right dono subtree check karo
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Recursion ka golden rule: Aap sirf current node ki responsibility lo, baaki recursion par chhod do.

# Recursively compare both trees node by node, checking that their structure
# and corresponding values are identical. If both nodes are empty they match;
# otherwise, any missing node or different value means the trees are different.
# Time: O(n), Space: O(h) where h is the tree height.