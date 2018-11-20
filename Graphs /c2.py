# DFS
from collections import defaultdict

class Graph:

    # constructor
    def __init__(self):
        self.graph = defaultdict(list) # values in the dict will be in form of a dict

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function to print a BFS of a graph
    def DFS(self, s):
        visited = [False] * len(self.graph)
        stack = []

        stack.append(s)
        visited[s] = True

        while stack:
            s = stack.pop(0)
            print(s, end=' ')

            start = 0
            for i in self.graph[s]:
                if visited[i] == False:
                    stack.insert(start, i)
                    start = start + 1
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS traversal starting from vertex 2")
g.DFS(2)
