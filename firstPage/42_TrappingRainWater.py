class Solution:
    def find_next_height(self,heights,start,height):
        for i in range(start+1,len(heights)):
            if heights[i]>=height:
                return i
        return -1

    def find_max_index(self,heights):
        max_index=0
        for index,value in enumerate(heights):
            if heights[index]>heights[max_index]:
                max_index=index
        return max_index

    def help(self,sub_heights):
        res=0
        start=0
        while start<len(sub_heights):
            if sub_heights[start]==0:
                start+=1
            else:
                break
        i=start
        while i <len(sub_heights):
            next=self.find_next_height(sub_heights,start,sub_heights[start])
            if next==-1:
                return res
            else:
                res+=min(sub_heights[start],sub_heights[next])*(next-start)-sum(sub_heights[start:next])
                i=start=next
        return res

    def trap(self, heights):
        i=0
        start=0
        if len(heights)<=2:
            return 0
        max_index = self.find_max_index(heights)
        res = 0
        if max_index==len(heights)-1:
            return self.help(heights)
        else:
            res+=self.help(heights[0:max_index+1])
            res+=self.help(list(reversed(heights[max_index:])))
        return res



s=Solution()
print(s.trap([]))
print(s.trap([4,2,3]))
print(s.trap([0,2,0]))
print(s.trap([4,2,3]))
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))