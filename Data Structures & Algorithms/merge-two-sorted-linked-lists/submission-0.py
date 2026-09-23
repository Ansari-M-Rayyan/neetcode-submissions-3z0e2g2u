# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next

# Merge two sorted linked lists by repeatedly comparing their current nodes
# and attaching the smaller one to the result list.
# Once one list is exhausted, attach the remaining nodes of the other list.
# Time: O(n + m), Space: O(1)

"""
Step-by-Step Logic
1) Ek fake/dummy node create karo: dummy = ListNode(0) aur pointer tail = dummy.

2) Jab tak dono list1 aur list2 exist karte hain (while list1 and list2:):

    Agar list1.val <= list2.val, toh tail.next = list1, aur list1 = list1.next.

    Else, tail.next = list2, aur list2 = list2.next.

    Har bar tail = tail.next aage move karo.

3) Jab loop khatam ho, toh ho sakta hai kisi ek list ke elements bach gaye hon. Jo bhi bacha hai usko direct link kar do:

    tail.next = list1 if list1 else list2

4) Result ka original head dummy ke agle node par hoga, toh return karo: dummy.next.
"""