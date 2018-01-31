class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''
        m={}
        for num in nums:
            if num not in m:
                m[num]=1
            else:
                return True
        return False
        '''
        return len(nums) != len(set(nums))

s=Solution()
print(s.containsDuplicate([1,2,3,3,4]))
