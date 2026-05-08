class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        ans=0
        freq={}
        mf=0
        for r in range(len(s)):
            ch=s[r]
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1 
            mf=max(mf,freq[ch])
            while(r-left+1)-mf>k:
                freq[s[left]]-=1
                left+=1
            ans=max(ans,r-left+1)
        return ans
