class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        ans=""
        for word in dictionary:
            i=0
            j=0
            while i<len(s) and j<len(word):
                if s[i]==word[j]: #check if character in s matches the character in word then move both pointers else move only i
                    j+=1
                i+=1
                if j==len(word): #if we have traversed the whole word then we check if tis length is greater then ans
                    if len(word)>len(ans):
                        ans=word
                    elif len(word)==len(ans):
                        ans=min(ans,word) #if ans length is same as word then we take lexicographically smaller one
        return ans