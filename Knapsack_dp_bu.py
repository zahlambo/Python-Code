
def knapSack(S, w, v, n): 
	K = [[0 for x in range(S+1)] for x in range(n+1)] 
	
	for i in range(n+1): 
		for S in range(S+1): 
			
			
			if i==0 or S==0: 
				K[i][S] = 0
			elif w[i-1] <= S:
				print("if",K,[i],[S]) 
				K[i][S] = max(v[i-1] + K[i-1][S-w[i-1]], K[i-1][S]) 
			else: 
				K[i][S] = K[i-1][S]
				print("else",K,[i],[S]) 

	
	return K[n][S] 

v = [60, 100, 120] 
w = [10, 20, 30] 
S = 50
n = len(v) 
print(knapSack(S, w, v, n)) 
