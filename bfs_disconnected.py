#bfs is level order traversal for that we need enqueue
import queue 
from collections import defaultdict

class Graph:
    # A utility function to add an edge 
    # in an undirected graph.
    def __init__(self): 

        self.graph = defaultdict(list)
        #store graph 

    def addEdge(self, u, v): 
        self.graph[u].append(v)
        #add edge to graph
        
    def BFSUtil(self,u, visited): 

        # Create a queue for BFS 

        q = queue.Queue() 
        
        # Mark the current node as visited 
        # and enqueue it 
        visited[u] = True
        q.put(u) 
        
        while(not q.empty()): 
            
            # Dequeue a vertex from queue 
            # and print it 
            u = q.queue[0] 
            print(u, end = " ") 
            q.get() 
        
            # Get all adjacent vertices of the 
            # dequeued vertex s. If an adjacent 
            # has not been visited, then mark 
            # it visited and enqueue it 
         
            tv=len(self.graph)
            for i in range(tv): #run for num of vertices
                if visited[i]==False:
                    self.BFSUtil(i,visited)

    # This function does BFSUtil() for all 
    # unvisited vertices. 
    def BFS(self): 
        tv=len(self.graph)


        visited = [False] * tv 
        for u in range(tv): 
            if (visited[u] == False): 
                self.BFSUtil(u,visited)

# Driver code 
if __name__ == '__main__': 
    g=Graph()
    while(1):
        print("1.add edge 2.print 3.stop")
        x=int(input())
        if x==1:
            print("Input adge:")
            a=int(input())
            b=int(input())
            g.addEdge(a,b)

        elif x==2:
            g.BFS()
            print("\n")

        elif x==3:
            break

        else:
            continue







# # Python3 implementation of modified BFS 
# import queue 

# # A utility function to add an edge 
# # in an undirected graph. 
# def addEdge(adj, u, v): 
# 	adj[u].append(v) 

# # A utility function to do BFS of 
# # graph from a given vertex u. 
# def BFSUtil(u, adj, visited): 

# 	# Create a queue for BFS 
# 	q = queue.Queue() 
	
# 	# Mark the current node as visited 
# 	# and enqueue it 
# 	visited[u] = True
# 	q.put(u) 
# 	``
# 	# 'i' will be used to get all adjacent 
# 	# vertices 4 of a vertex list<int>::iterator i 
	
# 	while(not q.empty()): 
		
# 		# Dequeue a vertex from queue 
# 		# and print it 
# 		u = q.queue[0] 
# 		print(u, end = " ") 
# 		q.get() 
	
# 		# Get all adjacent vertices of the 
# 		# dequeued vertex s. If an adjacent 
# 		# has not been visited, then mark 
# 		# it visited and enqueue it 
# 		i = 0
# 		while i != len(adj[u]): 
# 			if (not visited[adj[u][i]]): 
# 					visited[adj[u][i]] = True
# 					q.put(adj[u][i]) 
# 			i += 1

# # This function does BFSUtil() for all 
# # unvisited vertices. 
# def BFS(adj, V): 
# 	visited = [False] * V 
# 	for u in range(V): 
# 		if (visited[u] == False): 
# 			BFSUtil(u, adj, visited) 

# # Driver code 
# if __name__ == '__main__': 

# 	V = 5
# 	adj = [[] for i in range(V)] 

# 	addEdge(adj, 0, 4) 
# 	addEdge(adj, 1, 2) 
# 	addEdge(adj, 1, 3) 
# 	addEdge(adj, 1, 4) 
# 	addEdge(adj, 2, 3) 
# 	addEdge(adj, 3, 4) 
# 	BFS(adj, V) 

# # This code is contributed by PranchalK 
