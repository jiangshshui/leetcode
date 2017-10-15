class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i=0
        count=0
        while i<len(nums):
            newstart=i
            while newstart+1<len(nums) and nums[newstart]==nums[newstart+1]:
                newstart+=1
            del nums[i:newstart]
            count+=1
            i+=1
        return count


s=Solution()
print(s.removeDuplicates([1,2,2,3,3,3,4]))