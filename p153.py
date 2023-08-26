#858

'''
Python program for Topological Sorting
'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def topologocalSortUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topologocalSortUtil(i,visited,stack)

        stack.insert(0,v)

    def topologicalSort(self):
        visited = [False]*self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologocalSortUtil(i,visited,stack)

        print(stack)

g = Graph(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)

print("Following is a topological sort of the given graph")

g.topologicalSort()

################################################################################################################

#859

'''
Non-recursive Topological sorting
'''

from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def neighbor_gen(self,v):
        for k in self.graph[v]:
            yield k

    def nonRecursiveTopologicalSortUtil(self,v,visited,stack):
        working_stack = [(v, self.neighbor_gen(v))]

        while working_stack:
            v, gen = working_stack.pop()
            visited[v] = True

            for next_neighbor in gen:
                if not visited[next_neighbor]:
                    working_stack.append((v,gen))
                    working_stack.append((next_neighbor, self.neighbor_gen(next_neighbor)))
                    break
            else:
                stack.append(v)

    def nonRecursiveTopologicalSort(self):
        visited = [False]*self.V
        stack = []

        for i in range(self.V):
            if not(visited[i]):
                self.nonRecursiveTopologicalSortUtil(i, visited,stack)
        stack.reverse()
        print(stack)

g = Graph(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)

print("Following is a topological sort of the given graph")

g.nonRecursiveTopologicalSort()

################################################################################################################
















































































































































































