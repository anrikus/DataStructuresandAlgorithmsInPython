def recursive_unique(s1, s2=None):

    if s2==None:
        for i, x in enumerate(s1):
            unique = recursive_unique(s1[:i]+s1[i+1:], x)
            if unique != None:
                return(unique)
        return(None)

    else:
        for x in s1:
            if s2==x:
                return(None)
        return(s2)
