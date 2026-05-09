class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left=0
        cnt=0
        freq={'a':0,'b':0,'c':0}
        for r in range(len(s)):
            freq[s[r]]+=1 #move right pointer forward and update freq
            while freq['a']>0 and  freq['b']>0 and  freq['c']>0: #all charaters freq must be greater than 1
                cnt+=len(s)-r #cnt gets calculated when each char freq is greater than 1 
                freq[s[left]]-=1  #shrink left and update freq
                left+=1
        return cnt

