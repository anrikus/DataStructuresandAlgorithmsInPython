def factors(n):
    k = 1
    rem_factors=[]
    while k*k<n:
        if n%k == 0:
            rem_factors+=[n//k]
            yield k
        k+=1
    if k*k == n:
        yield k
    for x in rem_factors[-1::-1]:
        yield x
            
