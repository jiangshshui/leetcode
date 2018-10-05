class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five=ten=0

        for bill in bills:
            if bill==5:
                five+=1
            else:
                if bill==10:
                    if five>=1:
                        five-=1
                        ten+=1
                    else:
                        return False
                if bill==20:
                    if five>=1 and ten>=1:
                        ten-=1
                        five-=1
                    elif five>=3:
                        five-=3
                    else:
                        return False
        return True



if __name__=="__main__":
    s=Solution()
    print(s.lemonadeChange([5,5,5,10,20]))
    print(s.lemonadeChange([5,5,10]))
    print(s.lemonadeChange([10,10]))
    print(s.lemonadeChange([5,5,10,10,20]))