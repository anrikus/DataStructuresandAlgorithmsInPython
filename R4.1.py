def maximum(a):

    if len(a)==1:
        return(a[0])

    elif len(a)==2:
        return(max(a[0],a[1]))

    else:
        return(max(a[0], maximum(a[1:])))
