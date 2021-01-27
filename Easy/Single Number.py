class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            if num in temp: # second occurrence of element
                temp.remove(num) 
            else:
                temp.append(num) # first occurrence of element
        
        return temp[0]
