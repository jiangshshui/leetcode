class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x==-2**32:
        #     return False
        if x<0:
            return False
        x=abs(x)
        len=0
        temp=x
        while(temp):
            len+=1
            temp=temp//10
        i=1
        temp1,temp2=x,x
        while(i<=len):
            tempi=temp1%10
            templen=temp2//(10**(len-1))
            temp1=temp1//10
            temp2=temp2-templen*(10**(len-1))
            i+=1
            len-=1
            if(tempi==templen):
                continue
            else:
                return False
        return True


    #bestAnswer
    # def isPalindrome(self, x):
    #     if x < 0:
    #         return False
    #
    #     ranger = 1
    #     while x / ranger >= 10:
    #         ranger *= 10
    #
    #     while x:
    #         left = x / ranger
    #         right = x % 10
    #         if left != right:
    #             return False
    #
    #         x = (x % ranger) / 10
    #         ranger /= 100
    #
    #     return True
s=Solution()
print(s.isPalindrome(10))