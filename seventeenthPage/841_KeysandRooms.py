class Solution:
    def dfs(self,rooms,visited,curindex):
        for item in rooms[curindex]:
            if visited[item]==False:
                visited[item]=True
                self.dfs(rooms,visited,item)
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited=[False for _ in range(len(rooms))]
        visited[0]=True
        self.dfs(rooms,visited,0)
        for i in range(len(visited)):
            if visited[i]==False:
                return False
        return True



s=Solution()
print(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))