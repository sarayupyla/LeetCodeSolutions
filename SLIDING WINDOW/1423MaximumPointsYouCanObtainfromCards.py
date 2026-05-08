class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if k==n:
            return sum(cardPoints)
        total_sum=sum(cardPoints)
        win_size=n-k
        win_sum=sum(cardPoints[:win_size])
        min_sum=win_sum
        left=0
        for right in range(win_size,n):
            win_sum+=cardPoints[right]
            win_sum-=cardPoints[left]
            left+=1
            min_sum=min(min_sum,win_sum)
        return total_sum-min_sum
      
