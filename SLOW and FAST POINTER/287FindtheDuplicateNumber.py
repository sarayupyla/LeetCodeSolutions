class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    #solved this prob by 2 approaches and 3 solutions
    #first approach is by using set and 2nd approach is by using slow and fast pointer
        '''seen=set()
        for num in nums:
            if num in seen: #if that alue already in set then we got the duplicate number
                return num
            seen.add(num)    
    #by using slow and fast pointer as sets take extra space
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow] #slow moves on step
            fast=nums[nums[fast]] #fast moves two steps
            if fast==slow:
            return slow #when both meet we say the duplicate number is found 
        '''
    #for few other cases it doesnt work then we use temp(second phase)
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if fast==slow:
                break 
        temp=nums[0] #we start temp from start and slow from meeting point 
        while temp!=slow:
            temp=nums[temp] #we move both temp and slow one step at a time and when they meet we get the duplicate number
            slow=nums[slow]
        return slow
