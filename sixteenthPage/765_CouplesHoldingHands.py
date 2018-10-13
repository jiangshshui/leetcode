class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ptn=[]
        pos=[0 for i in range(len(row))]
        for i in range(len(row)):
            ptn.append(i+1 if i%2==0 else i-1)
            pos[row[i]]=i

        res=0
        for i in range(len(row)):
            j=ptn[pos[ptn[row[i]]]]
            while j!=i:
                pos[row[i]], pos[row[j]] = pos[row[j]], pos[row[i]]
                row[i],row[j]=row[j],row[i]
                res+=1
                j = ptn[pos[ptn[row[i]]]]
        return res


if __name__=="__main__":
    s=Solution()
    print(s.minSwapsCouples([3,9,10,5,0,4,11,16,6,2,1,17,18,13,7,19,14,8,15,12]))