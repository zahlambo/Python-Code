def hash(k,i):
    res=( (2*k + 7)%11 + i*(k+5)%11 )%11
    return res

print(hash(12,0))