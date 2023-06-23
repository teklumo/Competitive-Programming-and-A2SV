class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for n in range(len(nums)-1):
            if nums[n]==0:
                for m in range(n+1,len(nums)):
                    if nums[m]!=0:
                        nums[n],nums[m]=nums[m],nums[n]
                        break