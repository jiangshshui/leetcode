class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emps={employee.id:employee for employee in employees}
        def dfs(id):
            subordinates_importance=sum([dfs(sub_id) for sub_id in emps[id].subordinates])
            return emps[id].importance+subordinates_importance
        return dfs(id)
s=Solution()
print(s.getImportance())