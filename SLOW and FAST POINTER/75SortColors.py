class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''we use 3 pointers '''
        zero=0
        one=0
        two=0
        for num in nums:
            if num==0:
                zero+=1
            elif num==1:
                one+=1
            else:
                two+=1
        nums[:]=[0]*zero+[1]*one+[2]*two   #modify the original array 