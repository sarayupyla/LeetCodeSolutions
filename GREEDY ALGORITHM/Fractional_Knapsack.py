class Solution:
    def fractionalKnapsack(self, val, wt, cap):
        arr=[]
        for i in range(len(val)):
            ratio=val[i]/wt[i]   #take ratio to know how much value we get per unit weight
            arr.append((ratio,val[i],wt[i]))  #store the ratio,value and weight in list
        arr.sort(reverse=True)  #sort in decending order 
        ans=0
        for ratio,value,weight in arr:
            if cap>=weight:  #if the weight is less that or equal to capacity 
                ans+=value   #add the value  
                cap-=weight  #reduce the capacity by the weight which we have already taken
            else:
                ans+=ratio*cap   #if the weight is greater than capacity we take sufficient weight to fill the capacity and add the value
                break
        return round(ans,6)  