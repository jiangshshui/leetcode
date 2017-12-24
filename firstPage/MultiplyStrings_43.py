class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # if num1=='0' or num2=='0':
        #     return '0'
        num1=list(reversed(num1))
        num2=list(reversed(num2))
        sum=[0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                sum[i+j]+=int(num1[i])*int(num2[j])
        res=''
        carry=0
        for num in sum:
            res+=str((carry+num)%10)
            carry=(carry+num)//10

        while len(res)>1 and res[-1]=='0':
            res=res[:-1]
        res=res[::-1]
        # if res[0]=='0':
        #     return res[1:]
        return res


s=Solution()
print(s.multiply("9999","0"))


#http://www.cnblogs.com/TenosDoIt/p/3735309.html
