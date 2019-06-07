def __mul__(self, other):
    if not isinstance(other, int):
        raise ValueError("Multiplier must be integer")
    
    result = Vector(len(self))

    for j in len(self):
        result[j]=self[j]*3

    return(result)
