class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        r=0
        total=0
        ans=float('inf')  #assign the ans to highest value possible 
        for l in range(len(nums)):
            total+=nums[l]  # add the values to reach value greater than or equal to target
            while total>=target:
                ans=min(ans,l-r+1) #update min value for every subarray that meets the condition
                total-=nums[r] #reduce the right most value from total to move to next subarray 
                r+=1
        if ans==float('inf'): #if no subarray leads to target 
            return 0
        return ans