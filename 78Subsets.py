class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def generate(ind,subset,ans,nums):
            if(ind==len(nums)): #indec reached out of the bounds
                ans.append(subset.copy()) #duplicate cause it doesnt effect ans
                return
            subset.append(nums[ind])
            generate(ind+1,subset,ans,nums) #take towards left
            subset.pop()  
            generate(ind+1,subset,ans,nums) #not take right
        ind=0
        ans=[]
        subset=[]
        generate(ind,subset,ans,nums)
        return ans