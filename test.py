import math
# def fun(n):
#     if n==0:
#         return
#     print(n%2)

#     fun(math.floor(n/2))


# fun(25)
# def sumc(a,b):
#     return a+b

# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# def calculate(a,b):
#     print("Substitution",sub(a,b))
#     print("Sumation",sumc(a,b))
#     print("multipication",mul(a,b))
#     print("Division",div(a,b))

# calculate(1040,850)
# Fibonacci Series using Dynamic Programming 
def fibonacci(n): 
	
	# Taking 1st two fibonacci nubers as 0 and 1 
	FibArray = [0, 1] 
	
	while len(FibArray) < n + 1: 
		FibArray.append(0) 
	
	if n <= 1: 
		return n 
	else: 
		if FibArray[n - 1] == 0: 
			FibArray[n - 1] = fibonacci(n - 1) 

		if FibArray[n - 2] == 0: 
			FibArray[n - 2] = fibonacci(n - 2) 
			
	FibArray[n] = FibArray[n - 2] + FibArray[n - 1] 
	return FibArray[n] 
	
# for i in range(1,1001):
#     print(i,":",fibonacci(i))
print(fibonacci(100))
