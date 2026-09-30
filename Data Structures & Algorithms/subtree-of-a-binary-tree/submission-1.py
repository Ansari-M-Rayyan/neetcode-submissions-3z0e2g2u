# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Cases:
        # Empty tree subRoot hamesha kisi bhi tree ka subtree hota hai
        if not subRoot:
            return True
        # Agar main root empty ho gaya par subRoot abhi bhi bacha hai -> No match
        if not root:
            return False

        # 1. Kya current root par exact match mil gaya?
        if self.isSameTree(root, subRoot):
            return True

        # 2. Agar current root par match nahi mila,
        # toh check karo kya left ya right subtree mein kahi match milta hai
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # Helper function: LeetCode 100 (Same Tree)
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

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)