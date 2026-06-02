class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def fun(dica,dicb):
            if len(dica)!=len(dicb): 
                return False
            for i in dica:
                if i not in dicb or dica[i]!=dicb[i]:  #if the char is not in dicb or the freq of char in window is not same as freq of char in p
                    return False
            return True
        dica={}
        dicb={}
        for i in p:  #store the freq of each character of p in dicb
            if i in dicb:
                dicb[i]+=1
            else:
                dicb[i]=1
        l=0
        ans=[]
        for r in range(len(s)):  
            if s[r] in dica:
                dica[s[r]]+=1
            else:
                dica[s[r]]=1
            if r-l+1>len(p):  #if the window size is greater than p we remove the leftmost character from the window
                dica[s[l]]-=1 #reduce the freq of leftmost char by 1
                if dica[s[l]]==0:  #if the freq becomes 0 we remove it from dica
                    dica.pop(s[l])
                l+=1
            if r-l+1==len(p): #if the window size is equal to p we check if the freq of char in window is same as freq of char in p
                if fun(dica,dicb):
                    ans.append(l) #if condition is True we add the starting index of window to ans
        return ans