class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans=0
        ps=0
        freq={0:1} #empty prefix exist once
        for num in nums:
            ps+=num #update prefix sum while moving forward
            if ps-goal in freq: #if ps-goal exist that maeans we got a subarray with sum=goal
                ans+=freq[ps-goal]
            if ps in freq: #if the prefix  sum val already exists then increase
                freq[ps]+=1
            else:
                freq[ps]=1
        return ans
