class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        orAll=0
        for x in nums:
            orAll|=x 
        return orAll<<(n-1)       