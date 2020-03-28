from collections import defaultdict
#to make a adjacency list

class Graph:
    def __init__(self):
        
        self.graph=defaultdict(list)

        #store graph as an adjacency list


    def addedge(self,u,v):

        self.graph[u].append(v)

        #this add edge to the graph

    
    def dfsvisited(self,v,visited):

        #mark node as visited and print it

        visited[v]=True
        print(v)

        # Recur for all the vertices adjacent to 
        # this vertex

        for i in self.graph[v]: #run for num of vertices
            if visited[i]==False:
                self.dfsvisited(i,visited)


    def dfs(self):
        tv=len(self.graph)#total vertices

        #mark all as not visited

        visited=[False]*(tv)
        
        # Call the recursive helper function to print 
		# DFS traversal starting from all vertices one 
		# by one 

        for i in range(tv):
            if visited[i]==False:
                self.dfsvisited(i,visited)

        #if graph is not disconnected we dont need this loop
        #visited = [False] * (len(self.graph)) 
		#self.DFSUtil(v, visited) 

#main
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
            g.dfs()
            print("\n")

        elif x==3:
            break

        else:
            continue
