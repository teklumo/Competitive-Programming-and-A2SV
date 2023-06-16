class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2=set(nums2)
        nums1=set(nums1)
        result=list(nums1 & nums2 )
        return result