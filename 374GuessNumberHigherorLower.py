# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left<=right:  #loop checks numbers from 1<=n
            mid=(left+right)//2   
            result=guess(mid)  #guess the number and store the result in result
            if result==0:
                return mid   #if ur guess is right 
            elif result==1:
                 left=mid+1 #if the number guessed is smaller then no.picked then you have to check numbers greater than mid
            else:
                right=mid-1 #if number guessed is greater than no.picked then you have to check numbers smaller than mid