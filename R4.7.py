def strtoint(x):
    if x=="":
        return(0)
    else:
        return((ord(x[0])-48)*(10**len(x[1:]))+strtoint(x[1:]))
    
