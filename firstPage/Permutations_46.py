class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1:
            return [nums]
        res=[]
        for i in range(len(nums)):
            tempres=self.permute(nums[0:i]+nums[i+1:len(nums)])
            for item in tempres:
                item.append(nums[i])
                res.append(item)
        return res

s=Solution()
print(s.permute([1,2,3]))
