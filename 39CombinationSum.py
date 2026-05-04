class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def generate(ind,comb,ans,candidates,target):
            if(target==0):  #when target is subtracted with the sum of elements we should get 0 then it gives perfect combination of elements
                ans.append(comb.copy())
                return
            if(target<0): #target cannot be negative
                return
            if(ind==len(candidates)): #out of bounds
                return
            comb.append(candidates[ind]) 
            generate(ind,comb,ans,candidates,target-candidates[ind]) #towards left you wont change indx cause a val can be used multiple times
            comb.pop()
            generate(ind+1,comb,ans,candidates,target)  #towards right you will change indx cause you have to take nct val sum
        ind=0
        ans=[]
        comb=[]
        generate(ind,comb,ans,candidates,target)
        return ans
         