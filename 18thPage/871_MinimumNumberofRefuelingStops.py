# class Solution:
#     def minRefuelStops(self, target, startFuel, stations):
#         """
#         :type target: int
#         :type startFuel: int
#         :type stations: List[List[int]]
#         :rtype: int
#         """
#         dp=[startFuel]+[0]*len(stations)
#         for i,(location,capacity) in enumerate(stations):
#             for t in range(i,-1,-1):
#                 if dp[t]>=location:
#                     dp[t+1]=max(dp[t+1],dp[t]+capacity)
#
#         for i,d in enumerate(dp):
#             if d>=target:
#                 return i
#
#         return -1

import heapq
class Solution(object):
    def minRefuelStops(self, target, tank, stations):
        pq = []  # A maxheap is simulated using negative values
        stations.append((target, float('inf')))
        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in past
                tank += -heapq.heappop(pq)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(pq, -capacity)
            prev = location
        return ans

if __name__=="__main__":
    s=Solution()
    #print(s.minRefuelStops(target = 100, tank = 10, stations = [[10,60],[20,30],[30,30],[60,40]]))
    print(s.minRefuelStops(100,50,[[25,25],[50,50]]))