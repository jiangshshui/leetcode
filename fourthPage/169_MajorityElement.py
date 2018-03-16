class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        thresh=length//2
        m={}
        for num in nums:
            if num not in m:
                m[num]=1
            else:
                m[num]+=1
            if m[num]>thresh:
                return num


s=Solution()
print(s.majorityElement())