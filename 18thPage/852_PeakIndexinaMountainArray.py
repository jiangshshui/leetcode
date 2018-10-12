class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mid,l,r=0,0,len(A)-1
        while l<r:
            mid=(l+r)//2
            if A[mid]>A[mid-1] and A[mid]<A[mid+1]:
                l=mid+1
            if A[mid]<A[mid-1] and A[mid]>A[mid+1]:
                r=mid
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                break
        return mid


if __name__=="__main__":
    s=Solution()
    print(s.peakIndexInMountainArray( [0,1,0]))
    print(s.peakIndexInMountainArray([0,2,1,0]))