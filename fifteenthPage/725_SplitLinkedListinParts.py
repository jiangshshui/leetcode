class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        length=0
        work=root
        while work:
            length+=1
            work=work.next

        num,l=length//k,length%k
        pre,cur=None,root
        ans=[]
        for i in range(k):
            l-=1
            ans.append(cur)
            pre=None
            for j in range(num+1 if l>=0 else num):
                pre=cur
                cur=cur.next
            if pre:
                pre.next=None
        return ans






# s=Solution()
# print(s.splitListToParts())