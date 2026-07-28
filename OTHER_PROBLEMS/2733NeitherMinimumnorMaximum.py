class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        nums.sort() #sorting the list so that the min and max elements will be at the edges so we can return other elements
        return nums[1] #after soring the 1st index contains neither min or max element so we can return that element