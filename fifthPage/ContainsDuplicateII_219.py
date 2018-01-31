class Solution(object):
    # def containsNearbyDuplicate(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: bool
    #     """
    #     m={}
    #     for index,num in enumerate(nums):
    #         if num not in m:
    #             m[num]=[index]
    #         else:
    #             m[num].append(index)
    #             m[num]=m[num]
    #     for value in m.values():
    #         if len(value)<=1:
    #             continue
    #         for i in range(len(value)-1):
    #             if value[i+1]-value[i]<=k:
    #                 return True
    #     return False
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m={}
        for index,value in enumerate(nums):
            if value not in m:
                m[value]=index
            else:
                if index-m[value]<=k:
                    return True
                else:
                    m[value]=index
        return False

s=Solution()
print(s.containsNearbyDuplicate([-1,-1],1))