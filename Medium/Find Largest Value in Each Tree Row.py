# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Reference: https://en.wikipedia.org/wiki/Breadth-first_search

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # note that the TreeNode class is not iterable 
        # i.e. Unable to be looped 
        
        result = []
        level = 0
        
        def LevelMaxSearcher(queue, level, result):
            if queue == None: # there is no branch or end of the tree
                return 
            elif level == len(result): # take the first value for that level
                result.append(queue.val)
            else: # compare all subsequent values with the above first value, and replace if larger 
                result[level] = max(result[level], queue.val)
            
            # search by levels 
            LevelMaxSearcher(queue.left, level+1, result)
            LevelMaxSearcher(queue.right, level+1, result)        
        
        LevelMaxSearcher(root, level, result)
        return result