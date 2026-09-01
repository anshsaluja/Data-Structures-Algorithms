# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            value1 = 0
            value2 = 0

            if l1:
                value1 = l1.val

            if l2:
                value2 = l2.val
            

            total = value1 + value2 + carry

            digit = total%10
            carry = total//10

            tail.next = ListNode(digit)
            tail = tail.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        
        return dummy.next
            


        