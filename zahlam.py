#note sir amar phone nosto hoye gese .
# sorry sir ami khatai like picture nite parsi nah
# tai code joma dite hosse

import sys
class DisjSet: 
	def __init__(self, n): 
	
		self.rank = [1] * n 
		self.parent = [i for i in range(n)] 



	def find(self, x):

		
		if (self.parent[x] != x):
			
			
			self.parent[x] = self.find(self.parent[x]) 
			
		return self.parent[x]
	
	def findmin(self, x,res):
		res=min(res,self.parent[x])
		#print(self.parent[x])

		if (self.parent[x] != x):
			
			
			self.parent[x] = self.findmin(self.parent[x],res) 
			
		
		return res

		

	def Union(self, x, y): 
	
	
		xset = self.find(x) 
		yset = self.find(y) 

		if xset == yset: 
			return

		if self.rank[xset] < self.rank[yset]: 
			self.parent[xset] = yset 

		elif self.rank[xset] > self.rank[yset]: 
			self.parent[yset] = xset 

		
		else: 
			self.parent[yset] = xset 
			self.rank[xset] = self.rank[xset] + 1
	
	

obj = DisjSet(8)
obj.Union(4, 3) 
obj.Union(4, 1)
obj.Union(7,2)
obj.Union(7,5) 
obj.Union(1,7)
print(obj.find(5))
print("min",obj.findmin(5,sys.maxsize))


