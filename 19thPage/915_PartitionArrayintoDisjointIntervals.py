class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        leftmax=[None]*len(A)
        rightmin=[None]*len(A)

        m=A[0]
        for i in range(len(A)):
            m=max(m,A[i])
            leftmax[i]=m

        m=A[-1]
        for i in range(len(A)-1,-1,-1):
            m=min(m,A[i])
            rightmin[i]=m

        for i in range(1,len(A)):
            if leftmax[i-1]<=rightmin[i]:
                return i



if __name__=="__main__":
    s=Solution()
    print(s.partitionDisjoint([1,1]))
    #print(s.partitionDisjoint([1,1,1,0,6,12]))