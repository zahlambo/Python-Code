def seidel(a, sol ,b): 
     
    n = len(a)      

    for j in range(0, n):        

        d = b[j]                 
        
        for i in range(0, n):    

            if(j != i): 

                d-=a[j][i] * sol[i] 

        sol[j] = d / a[j][j] 

    return sol   

if __name__ == "__main__":
         
                                
    a = []                           
    b = []  
    sol = [1, 0, 1]
    a = [[12 , 3, -5],[1, 5, 3],[3, 7, 13]] 
    b = [1,28,76]
    
    for i in range(1, 10+1):        

        sol = seidel(a, sol, b) 

        print(sol,"\n")
