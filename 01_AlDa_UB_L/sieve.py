def sieve(N):
    l = list(range(2,N))
    i=0
    while i<len(l):
        mult = l[i] 
        j=i+1
        while j<len(l): 
            if (l[j]%mult==0): l.pop(j)
            j+=1;
        i+=1
    return l
