def __mul__(self, other):
    if len(other)!=len(self):
        raise ValueError("Dimensions must agree")
    
    return(sum(x*y for x, y in self, other))
