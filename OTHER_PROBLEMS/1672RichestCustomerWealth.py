class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum=0
        for customer in accounts:
            total=0 
            for money in customer: 
                total+=money  #add money of each customer to get the total wealth
            maximum=max(maximum,total) #check the highest wealth of the customer and store it in maximum
        return maximum