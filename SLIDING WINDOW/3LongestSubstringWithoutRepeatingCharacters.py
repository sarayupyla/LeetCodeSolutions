class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      left=0
      ans=0
      val=set()
      for right in range(len(s)): 
        while s[right] in val:
            val.remove(s[left])  #if val already in set shrink left by removing the left character
            left+=1
        val.add(s[right])  
        ans=max(ans,right-left+1)
      return ans