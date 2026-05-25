class Solution:
    def countGoodSubstrings(self, s: str) -> int:
      c=0
      l=0
      val=set()
      for r in range(len(s)):
        while s[r] in val:
            val.remove(s[l]) #if we get duplicate character we remove left  and increment left
            l+=1
        val.add(s[r]) #distinct characters are added to set 
        if r-l+1>3:  #if window size is greater than 3 then we remove left most value 
            val.remove(s[l])
            l+=1
        if r-l+1==3: # we need window size of 3 and all distinct characters
            c+=1
      return c