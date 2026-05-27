class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(0,len(nums),2): #i values from 0,2,4,6...
            ans+=nums[i]
        return ans