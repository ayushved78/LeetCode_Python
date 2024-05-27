# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def devisor(a,b):
            while b:
                a, b = b, a % b
            return a
			
        cur = head 
        while cur.next:
            gcd_val = devisor(cur.val, cur.next.val)
            newNode = ListNode(gcd_val)
            newNode.next = cur.next
            cur.next = newNode
            cur = cur.next.next
        return head