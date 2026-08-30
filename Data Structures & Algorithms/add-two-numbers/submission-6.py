# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        res = ListNode(0, None)
        curr = res
        carry = 0

        while l1 or l2:

            add1 = l1.val if l1 else 0
            add2 = l2.val if l2 else 0
            sumL3 = add1 + add2 + curr.val
            sumVal = sumL3 % 10
            curr.val = sumVal
            carry = (sumL3 - sumVal) // 10
            print(sumL3, sumVal, carry)

            l1 = l1.next if l1 else None

            l2 = l2.next if l2 else None

            if l1 or l2 or carry != 0: 
                curr.next = ListNode(carry , None)
                curr = curr.next


        return res




        