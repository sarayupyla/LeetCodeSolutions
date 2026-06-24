class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay): 
            return -1 #if we can't make m bouquets with k flowers, we return -1
        else:
            left=min(bloomDay)  #we can make bouquet only after first flower blooms,so we start from that day
            right=max(bloomDay) #we can make bouquet only before last flower blooms,so we end at that day
            while left<right:
                mid=(left+right)//2
                bouquet=0
                flower=0
                for i in bloomDay:
                    if i<=mid: #if the flower blooms on or before mid day, we can use it to make a bouquet 
                        flower+=1
                        if flower==k: #if we have k flowers,we can make a bouquet
                            bouquet+=1
                            flower=0
                    else:
                        flower=0
                if bouquet>=m: #if we can make m bouquets on or before mid, we can try to find smaller day
                    right=mid
                else:
                    left=mid+1 #if we can't make m bouquets on or before mid, we need to try larger day
            return left