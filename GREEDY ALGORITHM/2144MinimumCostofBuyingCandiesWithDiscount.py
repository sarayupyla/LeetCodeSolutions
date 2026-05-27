class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort() 
        total=0
        count=0
        for i in range(len(cost)-1,-1,-1):  #we start from end of cost because we have to take costly candies first and skip 3rd 
            count+=1 #we count the number of candies we have taken and for every 3rd candy we skip cause its free
            if count%3!=0: #we add cost of candy to total if its not 3rd candy
                total+=cost[i]
        return total
                