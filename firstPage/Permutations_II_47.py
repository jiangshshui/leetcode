class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        nums=sorted(nums)
        i=0
        res=[]
        while i<len(nums):
           while i+1<len(nums) and nums[i]==nums[i+1]:
               i+=1
           restemp=self.permuteUnique(nums[0:i]+nums[i+1:len(nums)])
           for item in restemp:
               item.append(nums[i])
               res.insert(0,item)
           i+=1
        return res

s=Solution()
print(s.permuteUnique([1,1,2]))
