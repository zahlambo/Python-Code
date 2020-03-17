from functools import lru_cache

@lru_cache(1000)

def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
       return fibonacci(n-1)+fibonacci(n-2)
x=int(input())
for n in range (1,x+1):
    print(n,":",fibonacci(n))

# student =[("zahir",21,5.1,1),
# ("tarek",22,5.5,2),
# ("aysha",23,5.1,3)]

# size=lambda student: student[1]

# student.sort(key=size,reverse=True)
# print(student)