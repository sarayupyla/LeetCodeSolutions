class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        def next_index(i):
            return (i+nums[i])%n #to get next index value
        for i in range(n):
            slow=i
            fast=i
            direction=nums[i]>0 #to know the direction if +ve then we move forward else we move backward(-ve)
            while True:
                next_slow=next_index(slow)#move one step
                next_fast=next_index(fast)
                next_fast2=next_index(next_fast) #move 2 steps 
                if (nums[next_slow]>0)!=direction: #if the direction is different then we break 
                    break
                if (nums[next_fast]>0)!=direction: #if true!=true or false!=false then we dont break
                    break
                if (nums[next_fast2]>0)!=direction: #if true!=false or false!=true then we break
                    break
                slow=next_slow    #update slow pointer
                fast=next_fast2   #update fast pointer
                if slow==next_index(slow): #if we have only single element in the loop then we break as we need atleast 2 elements
                    break
                if slow==fast: #cycle exists 
                    return True
        return False