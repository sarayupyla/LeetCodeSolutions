class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten=0
        five=0
        for n in range(len(bills)):
            if bills[n]==5:  #5
                five+=1
            elif bills[n]==10:   #10
                ten+=1
                if five==0:
                    return False
                five-=1
            else:             #20
                if five>0 and ten>0: #if you have 5 and 10 then you can give 15 change to cutomer
                    five-=1
                    ten-=1
                elif five>=3: #even if you have no 10 but have three 5's then you can give 15 change
                    five-=3
                else:
                   return False
        return True
            
