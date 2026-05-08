class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        freq={}
        left=0
        ans=0
        for r in range(len(fruits)):
            if fruits[r] in freq:  #if fruit is already in freq then increase count
              freq[fruits[r]]+=1
            else:
               freq[fruits[r]]=1
            while len(freq)>2:  #if the freq has more then 2 fruits then shrink left
                 freq[fruits[left]]-=1 #remove the left fruit from freq
                 if freq[fruits[left]] ==0:   #if the freq of the shrinked fruit is 0 then remove it from freq
                    del freq[fruits[left]]
                 left+=1
            ans=max(ans,r-left+1)
        return ans

