#note:- Sir amar phone nosto hoiya gese.
# tai code e dite hoilo amar .... 
# amar ase pase ekon smartphone nai je picture tule dibo 


from collections import defaultdict 
 
class Graph: 
 
	def __init__(self): 
		
		self.graph = defaultdict(list) 

	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	def dfshelper(self, v, visited): 
 
		visited[v] = True
		print(v, end = ' ') 
 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.dfshelper(i, visited) 
 
	def DFS(self, v): 

		visited = [False] * (len(self.graph)) 

		self.dfshelper(v, visited) 

if __name__ == "__main__":
	
	g = Graph() 

	while 1:
		print("1.add edge 2.print 3.exit\n")
		n=int(input())
		if n==1:
			a,b=input("Input two edge with space\n").split(" ")
			g.addEdge(a,b)
		elif n==2:
			a=int(input("Select an strating point\n"))

			g.DFS(a)
		elif n==3:
			break
		else:
			print("try between 1-3 \n")
			continue

 

