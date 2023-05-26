class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        result=[]
        for n in nums:
            result.append(int(n))
        result.sort()
        return f"{result[-k]}"
