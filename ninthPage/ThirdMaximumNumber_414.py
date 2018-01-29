# class Solution(object):
#     def thirdMax(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         isRevise=[False for _ in range(3)]
#         max_three=[-2**32 for _ in range(3)]
#         for num in nums:
#             if not isRevise[0]:
#                 #if num>max_three[0]:
#                 max_three[0]=num
#                 isRevise[0]=True
#             elif not isRevise[1]:
#                 if num==max_three[0]:
#                     continue
#                 if num>max_three[0]:
#                     max_three[1] = max_three[0]
#                     max_three[0]=num
#                 else:
#                     max_three[1]=num
#                 isRevise[1] = True
#             elif not isRevise[2]:
#                 if num==max_three[0] or num==max_three[1]:
#                     continue
#                 if num>max_three[0]:
#                     max_three[2]=max_three[1]
#                     max_three[1]=max_three[0]
#                     max_three[0]=num
#                 elif num>max_three[1]:
#                     max_three[2]=max_three[1]
#                     max_three[1]=num
#                 else:
#                     max_three[2]=num
#                 isRevise[2]=True
#             else:
#                 if num==max_three[0]or num==max_three[1]or num==max_three[2]:
#                     continue
#                 if num>max_three[0]:
#                     max_three[2]=max_three[1]
#                     max_three[1]=max_three[0]
#                     max_three[0]=num
#                 elif num>max_three[1]:
#                     max_three[2]=max_three[1]
#                     max_three[1]=num
#                 elif num>max_three[2]:
#                     max_three[2]=num
#         if isRevise[2]:
#             return max_three[2]
#         else:
#             return max_three[0]


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_max = None
        second_max = None
        third_max = None
        for num in nums:
            if first_max is None:
                first_max=num
            elif second_max is None:
                if num>first_max:
                    second_max=first_max
                    first_max=num
                elif num==first_max:
                    continue
                else:
                    second_max=num
            elif third_max is None:
                if num==first_max or num==second_max:
                    continue
                if num>first_max:
                    third_max=second_max
                    second_max=first_max
                    first_max=num
                elif num>second_max:
                    third_max=second_max
                    second_max=num
                else:
                    third_max=num
            else:
                if num==first_max or num==second_max or num==third_max:
                    continue
                if num>first_max:
                    third_max=second_max
                    second_max=first_max
                    first_max=num
                elif num>second_max:
                    third_max=second_max
                    second_max=num
                elif num>third_max:
                    third_max=num
        if third_max == None:
            return first_max
        return third_max


s=Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))
print(s.thirdMax([1,1, 2]))
print(s.thirdMax([1,2,2,5,3,5]))
print(s.thirdMax([5,2,4,1,3,6,0]))
print(s.thirdMax([5,2,2]))



