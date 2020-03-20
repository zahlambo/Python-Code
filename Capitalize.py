def solve(s):
    str= [i.strip().capitalize() for i in s.split() ]
    for i in str:
         s =s.replace(i.lower(),i)
    return s

    # full_name = s.split(' ')
    # return ' '.join((word.capitalize() for word in full_name))
    
 
 
 s="hello world"
 solve(s)
 #output == Hello World
