def reverse(s, start=None, end=None):

    if type(s)==str:
        s = list(s)
        start = 0
        end = -1

    if start>len(s)+end:
        return("".join(x for x in s))
    else:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
        return(reverse(s, start, end))

    
