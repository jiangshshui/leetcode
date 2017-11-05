from copy import deepcopy
# class Solution(object):
#     def subsets(self, nums):
#         res=[]
#         tempList=[]
#         self.generate_subsets(res,tempList,nums,0)
#         return res
#
#
#     def generate_subsets(self,res,tempList,nums,start):
#         newtempList = deepcopy(tempList)
#         res.append(newtempList)
#         for i in range(start,len(nums)):
#             newtempList.append(nums[i])
#             self.generate_subsets(res,newtempList,nums,i+1)
#             del(newtempList[-1])


class Solution(object):
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

s=Solution()
print(s.subsets([1,2,3]))