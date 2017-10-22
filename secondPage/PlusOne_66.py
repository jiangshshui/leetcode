class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=0
        sum=digits[-1]+1
        carry=sum//10
        digits[-1]=sum%10
        for i in range(len(digits)-2,-1,-1):
            sum=digits[i]+carry
            digits[i]=sum%10
            carry=sum//10
        if carry:
            digits.insert(0,carry)
        return digits

s=Solution()
l=s.plusOne([0])
print(l)