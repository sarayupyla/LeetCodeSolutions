class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if k==n:  #k value is same as len of cardpoints then we can do sum of all cards and return
            return sum(cardPoints)
        total_sum=sum(cardPoints) #used later for subtracting
        win_size=n-k  
        win_sum=sum(cardPoints[:win_size]) #sum of first winsize elements
        min_sum=win_sum #to know min value to subtract total-min to get required result
        left=0
        for right in range(win_size,n):
            win_sum+=cardPoints[right]  # moving the window forward by adding the right element
            win_sum-=cardPoints[left] #while window is moving forward the left pointer is shrinked
            left+=1  #after shrinking move left pointer forward
            min_sum=min(min_sum,win_sum)  #update min value
        return total_sum-min_sum 
