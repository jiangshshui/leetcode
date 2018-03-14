class Solution:
    def longestConsecutive(self, nums):
        res=0
        m={}
        for num in nums:
            if num not in m:
                left=m[num-1] if num-1 in m else 0
                right=m[num+1] if num+1 in m else 0
                temp=left+right+1
                res=max(temp,res)
                m[num]=temp
                m[num-left]=temp
                m[num+right]=temp
            else:
                continue
        return res

s=Solution()
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))