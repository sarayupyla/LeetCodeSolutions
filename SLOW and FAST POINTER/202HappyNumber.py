class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()#we use set cause few number will never be one and will be repeated 
        while n!=1 and n not in seen: 
            seen.add(n)
            total=0
            while n>0:
                digit=n%10 #get last digit
                total+=digit*digit #add square of that digit to total
                n=n//10 #get first digit 
            n=total #update n to total and repeat the process until n==1 
        return n==1 