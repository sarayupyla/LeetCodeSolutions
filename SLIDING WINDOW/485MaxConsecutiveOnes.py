class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        ml=0
        for r in range(len(nums)):
            if nums[r]==0:  #if we find zero move left pointer to r+1 and start counting
                l=r+1
            ml=max(ml,r-l+1) #maxlen of the consecutive once
        return ml