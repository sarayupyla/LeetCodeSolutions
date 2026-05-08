class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        for i in range(len(nums)):
          if nums[i] in s:  #if the val already exist in set 
            return True
          s.add(nums[i]) #if not add  the val to set
          if len(s) > k: #if the size of the set is greater than k value then remove the left element
            s.remove(nums[i-k])
        return False
