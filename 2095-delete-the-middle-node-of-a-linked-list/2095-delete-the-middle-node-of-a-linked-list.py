# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        slow = fast = head

        while fast != None:
            if fast.next == None:
                break
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if prev and slow:
            prev.next = slow.next
        else:
            return None
        
        return head