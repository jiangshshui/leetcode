class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[0]*k
        for i in range(k+1):
            if i>len(nums1) or k-i>len(nums2):
                continue
            else:
                ans=self.max_array(ans,self.merge(self.top_k_in_array(nums1,i),self.top_k_in_array(nums2,k-i)))
        return ans

    def max_array(self,arr1,arr2):
        for i in range(len(arr1)):
            if arr1[i]>arr2[i]:
                return arr1
            if arr1[i]<arr2[i]:
                return arr2
            i+=1
        return arr1


    def compare_two_arr(self,nums1,index1,nums2,index2):
        '''
        nums1 index1 之后的数组大于  nums2 index2 之后的数组
        return True
        else
        return False
        '''
        left1=len(nums1)-index1
        if left1<=0:
            return False
        left2=len(nums2)-index2
        if left2<=0:
            return True

        length=max(left1,left2)
        for i in range(length):
            digit1=nums1[index1+i] if index1+i<len(nums1) else 0
            digit2=nums2[index2+i] if index2+i<len(nums2) else 0
            if digit1!=digit2:
                return digit1>digit2

        return True

    def merge(self,num1,num2):
        res=[]
        i,j=0,0
        while i<len(num1) and j<len(num2):
            if self.compare_two_arr(num1,i,num2,j):
                res.append(num1[i])
                i+=1
            else:
                res.append(num2[j])
                j+=1
        if i<len(num1):
            res.extend(num1[i:])
        if j<len(num2):
            res.extend(num2[j:])
        return res

    def top_k_in_array(self,num,k):
        stack=[]
        length=len(num)
        pop_num=length-k
        i=0
        while i<length:
            while len(stack)!=0 and num[i]>stack[-1] and pop_num>0:
                stack.pop()
                pop_num-=1
            stack.append(num[i])
            i+=1
        return stack[0:k]



if __name__=="__main__":
    s=Solution()
    # print(s.top_k_in_array([7,2,4,6,5],4))
    #print(s.maxNumber([3, 4, 6, 5],[9, 1, 2, 5, 8, 3],5))
    #print(s.maxNumber([1, 2],[],2))
    print(s.maxNumber([2, 5, 6, 4, 4, 0],[7, 3, 8, 0, 6, 5, 7, 6, 2],15))

    print(s.maxNumber([2, 0, 2, 1, 2, 2, 2, 2, 0, 1, 0, 0, 2, 0, 2, 0, 2, 1, 0, 1, 1, 0, 1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 2, 1, 0, 0, 1, 2,
     1, 2, 2, 1, 1, 0, 1, 2, 0, 2, 0, 1, 2, 0, 2, 1, 1, 1, 2, 0, 0, 1, 0, 2, 1, 2, 0, 1, 0, 0, 0, 1, 2, 1, 0, 1, 1, 2,
     0, 2, 2, 0, 0, 1, 1, 2, 2, 1, 1, 2, 2, 1, 0, 1, 2, 0, 1, 2, 2, 0, 0, 0, 2, 0, 2, 0, 2, 2, 0, 1, 1, 1, 1, 2, 2, 2,
     2, 0, 0, 2, 2, 2, 2, 0, 2, 0, 1, 0, 0, 2, 1, 0, 0, 2, 0, 2, 1, 1, 1, 1, 0, 1, 2, 0, 2, 1, 0, 1, 1, 1, 0, 0, 2, 2,
     2, 0, 2, 1, 1, 1, 2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 2, 0, 2, 0, 2, 0, 0, 1, 0, 1, 1, 0, 0, 2, 1, 1, 2, 2, 2, 1, 2, 2,
     0, 0, 2, 1, 0, 2, 1, 2, 1, 1, 1, 0, 2, 0, 1, 1, 2, 1, 1, 0, 0, 1, 0, 1, 2, 2, 2, 0, 2, 2, 1, 0, 1, 2, 1, 2, 0, 2,
     2, 0, 1, 2, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 2, 1, 2, 0, 1, 1, 1, 2, 2, 2, 0, 2, 0, 2, 0, 2, 1, 1, 0, 2, 2, 2, 1, 0,
     2, 1, 2, 2, 2, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 2, 2, 0, 1, 2, 1, 0, 0, 2, 2, 2, 2, 1, 0, 2, 0, 1, 2, 0],
    [1, 1, 1, 0, 0, 1, 1, 0, 2, 1, 0, 1, 2, 1, 0, 2, 2, 1, 0, 2, 0, 1, 1, 0, 0, 2, 2, 0, 1, 0, 2, 0, 2, 2, 2, 2, 1, 1,
     1, 1, 0, 0, 0, 0, 2, 1, 0, 2, 1, 1, 2, 1, 2, 2, 0, 2, 1, 0, 2, 0, 0, 2, 0, 2, 2, 1, 0, 1, 0, 0, 2, 1, 1, 1, 2, 2,
     0, 0, 0, 1, 1, 2, 0, 2, 2, 0, 1, 0, 2, 1, 0, 2, 1, 1, 1, 0, 1, 1, 2, 0, 2, 0, 1, 1, 2, 0, 2, 0, 1, 2, 1, 0, 2, 0,
     1, 0, 0, 0, 1, 2, 1, 2, 0, 1, 2, 2, 1, 1, 0, 1, 2, 1, 0, 0, 1, 0, 2, 2, 1, 2, 2, 0, 0, 0, 2, 0, 0, 0, 1, 0, 2, 0,
     2, 1, 0, 0, 1, 2, 0, 1, 1, 0, 1, 0, 2, 2, 2, 1, 1, 0, 1, 1, 2, 1, 0, 2, 2, 2, 1, 2, 2, 2, 2, 0, 1, 1, 0, 1, 2, 1,
     2, 2, 0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 2, 1, 1, 0, 1, 2, 0, 1, 2, 1, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 1, 2, 0, 1, 1, 1,
     1, 0, 1, 2, 2, 1, 0, 1, 2, 2, 1, 2, 2, 2, 0, 2, 0, 1, 1, 2, 0, 0, 2, 2, 0, 1, 0, 2, 1, 0, 0, 1, 1, 1, 1, 0, 0, 2,
     2, 2, 2, 0, 0, 1, 2, 1, 1, 2, 0, 1, 2, 1, 0, 2, 0, 0, 2, 1, 1, 0, 2, 1, 1, 2, 2, 0, 1, 0, 2, 0, 1, 0],600))


"""
[2,1,1,1,0,2,1,2,2,2,2,0,1,0,0,2,0,2,0,2,1,0,1,1,0,1,0,1,2,1,1,1,0,1,2,2,1,0,0,1,2,1,2,2,1,1,0,1,2,0,2,0,1,2,
0,2,1,1,1,2,0,0,1,1,0,2,1,0,1,2,1,0,2,2,1,0,2,0,1,1,0,0,2,2,0,1,0,2,0,2,2,2,2,1,1,1,1,0,0,1,0,2,1,2,0,1,0,0,
0,1,2,1,0,1,1,2,0,2,2,0,0,1,1,2,2,1,1,2,2,1,0,1,2,0,1,2,2,0,0,0,2,0,2,0,2,2,0,1,1,1,1,2,2,2,2,0,0,2,2,2,2,0,
2,0,1,0,0,2,1,0,0,2,0,2,1,1,1,1,0,1,2,0,2,1,0,1,1,1,0,0,2,2,2,0,2,1,1,1,2,2,0,0,2,2,2,2,2,0,2,0,2,0,2,0,0,1,
0,1,1,0,0,2,1,1,2,2,2,1,2,2,0,0,2,1,0,2,1,2,1,1,1,0,2,0,1,1,2,1,1,0,0,1,0,1,2,2,2,0,2,2,1,0,1,2,1,2,0,2,2,0,
1,2,2,1,2,2,1,1,2,2,2,2,2,1,2,0,1,1,1,2,2,2,0,2,0,2,0,2,1,1,0,2,2,2,1,0,2,1,2,2,2,0,1,1,1,1,1,1,0,0,0,2,2,0,
1,2,1,0,0,2,2,2,2,1,0,2,0,1,2,0,0,0,0,2,1,0,2,1,1,2,1,2,2,0,2,1,0,2,0,0,2,0,2,2,1,0,1,0,0,2,1,1,1,2,2,0,0,0,
1,1,2,0,2,2,0,1,0,2,1,0,2,1,1,1,0,1,1,2,0,2,0,1,1,2,0,2,0,1,2,1,0,2,0,1,0,0,0,1,2,1,2,0,1,2,2,1,1,0,1,2,1,0,
0,1,0,2,2,1,2,2,0,0,0,2,0,0,0,1,0,2,0,2,1,0,0,1,2,0,1,1,0,1,0,2,2,2,1,1,0,1,1,2,1,0,2,2,2,1,2,2,2,2,0,1,1,0,
1,2,1,2,2,0,0,0,0,0,1,1,1,2,1,2,1,1,0,1,2,0,1,2,1,2,2,2,2,0,0,0,0,2,0,1,2,0,1,1,1,1,0,1,2,2,1,0,1,2,2,1,2,2,
2,0,2,0,1,1,2,0,0,2,2,0,1,0,2,1,0,0,1,1,1,1,0,0,2,2,2,2,0,0,1,2,1,1,2,0,1,2,1,0,2,0,0,2,1,1,0,2,1,1,2,2,0,1,
0,2,0,1,0,0]
"""


# def merge(self, num1, num2):
#     res = []
#     i, j = 0, 0
#     while i < len(num1) and j < len(num2):
#         if num1[i:] <= num2[j:]:
#             res.append(num2[j])
#             j += 1
#         elif num1[i:] > num2[j:]:
#             res.append(num1[i])
#             i += 1
#
#         else:
#             k, m = i + 1, j + 1
#             while k < len(num1) and m < len(num2) and num1[k] == num2[m]:
#                 k += 1
#                 m += 1
#             if k >= len(num1) and m >= len(num2):
#                 res.extend(num1[i:])
#                 res.extend(num2[j:])
#                 return res
#             if k >= len(num1) and m < len(num2):
#                 if num1[k - 1] >= num2[m]:
#                     res.append(num1[i])
#                     i += 1
#                 else:
#                     res.append(num2[j])
#                     j += 1
#             elif k < len(num1) and m >= len(num2):
#                 if num1[k] >= num2[m - 1]:
#                     res.append(num1[i])
#                     i += 1
#                 else:
#                     res.append(num2[j])
#                     j += 1
#             elif num1[k] > num2[m]:
#                 res.append(num1[i])
#                 i += 1
#             else:
#                 res.append(num2[j])
#                 j += 1
#     if i < len(num1):
#         res.extend(num1[i:])
#     if j < len(num2):
#         res.extend(num2[j:])
#     return res
