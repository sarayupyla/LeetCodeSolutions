class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]: #left subarray
                if nums[left]<=target<nums[mid]: #left subarray compared with target
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[right]: #right subarray compared with target 
                   left=mid+1
                else:
                    right=mid-1
        return -1
                
