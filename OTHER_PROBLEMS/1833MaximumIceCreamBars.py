class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for cost in costs:
            if coins>=cost: #satisfied until his coins are completed
                coins-=cost
                count+=1  #counts number of ice cream bars that he can purchase with the coins
            else:
                break #break the loop is the cost>coins so no need to check next other elements cause they will be higher anyways
        return count