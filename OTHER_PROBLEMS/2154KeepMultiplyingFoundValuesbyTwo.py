class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in range(len(nums)):
           if original == nums[i]: #if original value exists in nums then continue multiplying with 2
               original = 2 * original
        return original
           


