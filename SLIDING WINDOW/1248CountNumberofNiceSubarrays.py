class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans=0
        ps=0
        freq={0:1}
        for num in nums:
            if num%2==1: #we need only odd numbers
             ps+=1 
            if ps-k in freq:
                ans+=freq[ps-k] 
            if ps in freq:
                freq[ps]+=1
            else:
                freq[ps]=1
        return ans