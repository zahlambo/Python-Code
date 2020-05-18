from collections import defaultdict 


class Graph: 

	def __init__(self,vertices): 
		self.V= vertices 
		self.graph = defaultdict(list) 


	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	def find_parent(self, parent,i): 
		if parent[i] == -1: 
			return i 
		if parent[i]!= -1: 
			return self.find_parent(parent,parent[i]) 

	def union(self,parent,x,y): 
		x_set = self.find_parent(parent, x) 
		y_set = self.find_parent(parent, y) 
		parent[x_set] = y_set 


	def getset(self):
		return self.graph

g = Graph(3) 
g.addEdge(0, 1) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 

print(g.getset())