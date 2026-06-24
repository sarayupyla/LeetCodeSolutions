class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for i in operations:
            if i=="+": #add the sum of last 2 scores to the score list
                score.append(score[-1]+score[-2])
            elif i=="D": #double the last score and add it to the score list
                score.append(2* score[-1])
            elif i=="C":# remove the last score from the score list
                score.pop()
            else:
                score.append(int(i)) #add the integer score to the score list
        return sum(score) 
