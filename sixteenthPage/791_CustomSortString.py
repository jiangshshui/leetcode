
class Solution:

    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        s=set(S)
        mt={}
        for t in T:
            if t in mt:
                mt[t]+=1
            else:
                mt[t]=1
        res=""
        for sch in S:
            if sch in mt:
                res+=sch*mt[sch]
                mt.pop(sch)

        for key,value  in mt.items():
            res+=key*value
        # for key,value in mt.items():
        #     for i in range(value):
        #         newRes=[]
        #         for j in range(len(res)):
        #             for k in range(len(res[j])):
        #                 newRes.append("".join((res[j][0:k]+key+res[j][k:])))
        #         res=newRes

        return res


s=Solution()
print(s.customSortString("abc","abcde"))