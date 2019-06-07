def min_max_recursive(seq, minimum=None, maximum=None):

    if seq==[]:
        return(minimum, maximum)

    elif minimum==None and maximum==None:
        minimum=maximum=seq[0]
       
    elif seq[0]<minimum:
        minimum = seq[0]

    elif seq[0]>maximum:
        maximum = seq[0]

    return(min_max_recursive(seq[1:], minimum, maximum))
