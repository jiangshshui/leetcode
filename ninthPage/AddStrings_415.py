class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res=""
        i=len(num1)-1
        j=len(num2)-1
        carry=0
        while i>=0 and j>=0:
            temp=ord(num1[i])-ord('0')+ord(num2[j])-ord('0')+carry
            carry=temp//10
            res+=str(temp%10)
            i-=1
            j-=1
        while i>=0:
            temp = ord(num1[i]) - ord('0')  + carry
            carry = temp // 10
            res += str(temp % 10)
            i -= 1
        while j>=0:
            temp = ord(num2[j]) - ord('0')  + carry
            carry = temp // 10
            res += str(temp % 10)
            j -= 1
        if carry!=0:
            res+=str(carry)
        return "".join(reversed(res))

s=Solution()#                     1234567890
print(s.addStrings("9","9"))
