class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lengtha=len(a)#较短的长度
        lengthb=len(b)
        if lengtha>lengthb:
            lengtha,lengthb=lengthb,lengtha
            a,b=b,a
        a="0"*(lengthb-lengtha)+a
        carry=0
        i=lengthb-1
        res=""
        while i>=0:
            sum=int(a[i])+int(b[i])+carry
            res+=(str(sum%2))
            carry=sum//2
            i-=1
        if carry:
            res += "1"
            return res[::-1]
        else:
            return res[::-1]

# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return "{0:b}".format(int(a, 2) + int(b, 2))
s=Solution()
res=s.addBinary("110",'1111')
print(res)




'''
>>> print '{0:b}'.format(3)  
11  
>>> print '{0:c}'.format(30)  
  
>>> print '{0:d}'.format(3)  
3  
>>> print '{0:o}'.format(10)  
12  
>>> print '{0:x}'.format(30)  
1e  
>>> print '{0:e}'.format(3)  
3.000000e+00  
>>> print '{0:f}'.format(3)  
3.000000  
>>> print '{0:g}'.format(3)  
3  
>>> print '{0:n}'.format(3)  
3  
>>> print '{0:n}'.format(3.1415)  
3.1415  
>>> print '{0:%}'.format(3.15)  
315.000000% 
'''