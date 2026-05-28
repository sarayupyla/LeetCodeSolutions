class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ml=0
        l=0
        f=0
        for r in range(len(answerKey)): #for all false to change to true 
            if answerKey[r]=='F': 
                    f+=1
            while f>k:
                if answerKey[l]=='F':
                    f-=1
                l+=1
            ml=max(ml,r-l+1)
        l=0
        t=0
        for r in range(len(answerKey)): #for all true to change to false 
            if answerKey[r]=='T':
                    t+=1
            while t>k:
                if answerKey[l]=='T':
                    t-=1
                l+=1
            ml=max(ml,r-l+1)
        return ml #check max length of both cases and return the max of them
        