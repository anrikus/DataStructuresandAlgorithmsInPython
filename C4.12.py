def recursive_product(s1, s2, total=0):
    if s2>s1:
        s1, s2 = s2, s1
    if s2>0:
        return(recursive_product(s1, s2-1, total+s1))
    else:
        return(total)
