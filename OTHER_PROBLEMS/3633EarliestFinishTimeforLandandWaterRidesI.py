class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans=float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                #land ride to water ride
                land_finish=landStartTime[i]+landDuration[i]   #finish time of land ride
                water_start=max(land_finish,waterStartTime[j]) #start time of water ride will be max of finish time of land rideand start timeof water ride
                finish1=water_start+waterDuration[j]   #finish time of water ride
                #water ride to land ride
                water_finish=waterStartTime[j]+waterDuration[j]  #finish time of water ride
                land_start=max(water_finish,landStartTime[i]) #start time of land ride will be max of finish time of water ride and start time of land ride
                finish2=land_start+landDuration[i] #finish time of land ride
                ans=min(ans,finish1,finish2)
        return ans
