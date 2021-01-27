# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # we want to reverse the pointer to point to the previous value
        
        curr = head
        result = None
        while curr != None:
            temp = curr.next # hold remaining nodes
            curr.next = result # reverse the pointer here
            result = curr
            curr = temp # repeat for remaining nodes
        
        return result
