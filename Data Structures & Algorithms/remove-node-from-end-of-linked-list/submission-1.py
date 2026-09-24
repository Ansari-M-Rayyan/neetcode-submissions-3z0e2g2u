'''
2-pointer Intuition:

Agar fast pointer ko pehle hi n steps aage bhej diya jaye...

Aur phir fast aur slow dono ko ek-ek step aage badhaya jaye...

Jab fast end (last node ya None) tak pahuchega, slow exactly piche se n-th target node ke theek pehle wale node par hoga!

Isse list ki total length count karne ke liye pehla loop lagane ki zaroorat nahi padti.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # Step 1: Fast ko n steps aage le jao
        for _ in range(n):
            fast = fast.next

        # Step 2: Dono ko tab tak badhao jab tak fast list ke bahar na nikal jaye
        while fast:
            slow = slow.next
            fast = fast.next

        # Step 3: Target node ko bypass (delete) kar do
        slow.next = slow.next.next

        return dummy.next

# Use two pointers with a fixed gap of n nodes between them.
# Move fast n steps ahead, then move both pointers together until fast reaches
# the end. Slow will be positioned just before the Nth node from the end,
# allowing that node to be removed directly.
# Time: O(n), Space: O(1)
