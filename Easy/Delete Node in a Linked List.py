# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # change value of node to be delete with value of subsequent node
        node.val = node.next.val
        
        # change value of next at the node to be deleted with the next of subsequent node
        node.next = node.next.next
        
