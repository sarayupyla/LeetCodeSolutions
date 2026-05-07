class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        ml=0
        for r in range(len(nums)):
            if nums[r]==0:
                l=r+1
            ml=max(ml,r-l+1)
        return ml