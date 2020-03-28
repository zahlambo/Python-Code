# This code is contributed by Nikhil Kumar Singh 
def top_up(n,w,v,c,i):
    store = [[0 for x in range(c+1)] for x in range(n+1)] #c*n matrix values set to zero
    if i==n or c<=0:
        return 0
    if store[i][c]>0:  #if store has value then return
        return store[i][c]
    if w[i]<=c:
        vin=top_up(n,w,v,c-w[i],i+1)+v[i]#value if include
        vex=top_up(n,w,v,c,i+1)#if exclude 
       # return max(vin,vex)
        store[i][c]=max(vin,vex) #store max value
       
    else:
        vex=top_up(n,w,v,c, i+1)#if capacity exceed then exclude
        #return vex
        store[i][c]=vex
    return store[i][c]


w=[2,4,3,5,5]
v=[3,4,1,2,6]
c=12
print(top_up(len(w),w, v, c, 0))