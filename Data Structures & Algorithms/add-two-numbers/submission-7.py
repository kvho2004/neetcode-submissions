# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:   
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        curr = l3
        carr = 0
        while (l1 is not None or l2 is not None):
            sumN = curr.val
            if l1 is not None:
                sumN+= l1.val
                l1 = l1.next
            if l2 is not None:
                sumN+= l2.val
                l2 = l2.next

            curr.val = sumN % 10
            carr = sumN // 10

            if (l1 is None and l2 is None and carr == 0):
                break

            nex = ListNode(carr)
            curr.next = nex
            curr = curr.next


        return l3





        
        