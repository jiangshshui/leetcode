class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        accu_sum=[0]
        for a in A:
            accu_sum.append(accu_sum[-1]+a)

        left=0
        right=1
        ans=0
        while right<len(accu_sum):
            if left>=right and left<len(accu_sum):
                right+=1
                continue
            if accu_sum[right]-accu_sum[left]==S:
                ans+=1
                j=1
                while right+j<len(accu_sum) and accu_sum[right]==accu_sum[j+right]:
                    j+=1
                    ans+=1
                left=left+1
            elif accu_sum[right]-accu_sum[left]<S:
                right+=1
            else:
                left+=1
        return ans



if __name__=="__main__":
    s=Solution()
    print(s.numSubarraysWithSum(A = [1,0,1,0,1], S = 2))
    print(s.numSubarraysWithSum([0,0,0,0,0],0))