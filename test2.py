
def knapSack(W, wa, va, n): 

    p = [[0 for x in range(W+1)] for x in range(n+1)] 
    #print(p)
    # for W in range (W):
    #     #p[0,W]=0
    # for i in range (0,n+1):
        #p[i,0]=0
    for i in range(0,W+1):
        
            if wa[i]<=W:
                if  (v[i]+p[i-1,W-wa[i]])>(p[i-1,W]):
                    p[i,W]=v[i]+p[i-1,w-wa[i]]
                else:
                    p[i,w]=p[i-1,w]
            
            else:
                p[i,w]=p[i-1,w]


v = [60, 100, 120] 
w = [10, 20, 30] 
S = 50
n = len(v) 
print(knapSack(S, w, v, n)) 
