# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        print(root)
        def MaxDepthSearcher(queue, pointer, depth):
            if queue == None:
                return 
            elif queue.left == None and queue.right == None:
                return 
            else:
                pointer += 1
                if depth[0] < pointer: # check if the count is greater than current highest value
                    depth[0] = pointer # update highest value
            
            MaxDepthSearcher(queue.left, pointer, depth)
            MaxDepthSearcher(queue.right, pointer, depth)
        
        if root == None:
            return 0
        else:
            pointer = 1
            depth = [pointer] # use reference object to store output
            MaxDepthSearcher(root, pointer, depth)
            return depth[0]
