class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def __init__(self):
        self.m={}
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if node is None:
            return None
        if node.label in self.m:
            return self.m[node.label]

        clone=UndirectedGraphNode(node.label)
        self.m[node.label]=clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))
        return clone



s=Solution()
print(s.cloneGraph())

'''
public class Solution {
    private HashMap<Integer, UndirectedGraphNode> map = new HashMap<>();
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        return clone(node);
    }

    private UndirectedGraphNode clone(UndirectedGraphNode node) {
        if (node == null) return null;
        
        if (map.containsKey(node.label)) {
            return map.get(node.label);
        }
        UndirectedGraphNode clone = new UndirectedGraphNode(node.label);
        map.put(clone.label, clone);
        for (UndirectedGraphNode neighbor : node.neighbors) {
            clone.neighbors.add(clone(neighbor));
        }
        return clone;
    }
}
'''