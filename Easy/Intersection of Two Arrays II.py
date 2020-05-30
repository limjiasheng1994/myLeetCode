class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # start with the smaller array to optimize 
        if len(nums1) != len(nums2):
            compare = nums1 if len(nums1) < len(nums2) else nums2 
            alternative = nums1 if len(nums1) > len(nums2) else nums2
        else: 
            compare = nums1
            alternative = nums2
        
        # function to extract intersection 
        def computeIntersection(element, compare, alternative, result):
            totalInstances = min(compare.count(element), alternative.count(element))
            result.extend([element] * totalInstances)
        
        result = []
        for element in compare: 
            if element in result: 
                continue
            elif element in alternative:
                computeIntersection(element, compare, alternative, result)
                
        return result