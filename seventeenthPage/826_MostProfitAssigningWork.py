class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs=sorted([a,b] for a,b in zip(difficulty,profit))
        # return jobs
        i = 0
        max_p=0
        res=0
        for w in sorted(worker):
            while i<=len(jobs):
                if i<len(jobs) and w>=jobs[i][0]:
                    max_p=max(max_p,jobs[i][1])
                else:
                    res+=max_p
                    break
                i += 1
        return res

s=Solution()
#print(s.maxProfitAssignment([2,4,6,8,10,10],[10,20,30,40,50,40],[4,5,6,7]))
print(s.maxProfitAssignment([13,37,58],[4,90,96],[34,73,45]))