'''
效率低
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        position=[0 for _ in range(len(findNums))]
        res=[-1 for _ in range(len(findNums))]

        def findPosition(nums,target):
            for index in range(len(nums)):
                if nums[index]==target:
                    return index
            return -1

        for i in range(len(findNums)):
            position[i]=findPosition(nums,findNums[i])

        for i in range(len(position)):
            for j in range(position[i],len(nums)):
                if findNums[i]<nums[j]:
                    res[i]=nums[j]
                    break
        return res
'''

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        res=[-1 for _ in range(len(findNums))]
        stack=[]
        if len(nums)==0:
            return []
        stack.append(nums[0])
        j=1
        m={}
        while stack and j<len(nums):
            while stack and stack[-1]<nums[j]:
                m[stack.pop()]=nums[j]
            stack.append(nums[j])
            j+=1
        for index,num in enumerate(findNums):
            if num in m:
                res[index]=m[num]
        return res


s=Solution()
print(s.nextGreaterElement([],[]))
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))