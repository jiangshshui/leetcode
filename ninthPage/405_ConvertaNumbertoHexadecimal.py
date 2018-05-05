class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return "0"
        # m={}
        # for i in range(10):
        #     m[i]=str(i)
        # for i in range(10,16):
        #     m[i]=chr(97+i-10)
        m=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        res=""
        # if num<0:
        #     num=2**32+num
        n=0
        while n<8 and num:
            res=m[num%16]+res
            num//=16
            n+=1
        return res




s=Solution()
print(s.toHex(-1))

