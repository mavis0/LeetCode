# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.nodes = dict()

    def cloneGraph(self, node):
        if not node:return
        if node.label in self.nodes:
            return self.nodes[node.label]
        newNode = UndirectedGraphNode(node.label)
        self.nodes[node.label] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.cloneGraph(neighbor))
        return newNode
