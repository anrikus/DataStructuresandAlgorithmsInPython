def recursive_harmonic(n):
    if n!=1:
        return(1/n +recursive_harmonic(n-1))
    if n==1:
        return(1)
