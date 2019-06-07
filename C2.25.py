def __mul__(self, other):
    if isinstance(other, int):
        result = Vector(len(self))
        for j in len(self):
            result[j]=self[j]*3
        return(result)

    if len(other)!=len(self):
        raise ValueError("Dimensions must agree")
    
    return(sum(x*y for x, y in self, other))
