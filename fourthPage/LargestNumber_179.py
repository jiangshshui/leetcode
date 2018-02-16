'''
错误
# class Solution:
#     # @param {integer[]} nums
#     # @return {string}
#     def largestNumber(self, nums):
#         nums=sorted(nums,reverse=True)
#         max=nums[0]
#         maxlength=self.length(nums[0])
#         same_size_nums=[num*10**(maxlength-self.length(num)) for num in nums]
#         d=dict()
#         for i,num in enumerate(same_size_nums):
#             d[nums[i]]=num
#         d=sorted(d.items(),key=lambda item:(item[1],-self.length(item[0])),reverse=True)
#         res=""
#         for item in d:
#             res+=str(item[0])
#         return res
#
#     def length(self,num):
#         size=0
#         while num:
#             size+=1
#             num//=10
#         return size
'''



from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums):
        from functools import cmp_to_key
        #key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        #key = cmp_to_key(lambda x, y: int(y + x)-int(x + y))
        key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        nums=sorted(map(str, nums), key=key,reverse=True)
        res = ''.join(nums).lstrip('0')
        return res or '0'

s=Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))

'''
['3', '30', '34', '5', '9']
'''