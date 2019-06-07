def recursive_log(n):
    if n//2 == 0:
        return(0)
    else:
        return(1+recursive_log(n//2))
