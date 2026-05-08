class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
      ml=0
      left=0
      z=0
      for r in range(len(nums)):
        if nums[r]==0:
            z+=1  #if zero is found add it 
        while(z>k):  #the value of zero cannot be greater then k value
            if nums[left]==0:  #start shrinking left until you find zero
                z-=1 #if zero is found reduce it 
            left+=1
        ml=max(ml,r-left+1) #maxlen of the consecutive once with atmost k zero
      return ml 