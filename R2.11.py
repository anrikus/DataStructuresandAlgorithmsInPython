def __radd__(self, other):
    if len(self)!=len(other):
        raise ValueError("Dimensions must agree")

    result = Vector(len(self))

    for j in len(self):
        result[j]=other[j]+self[j]

    return(result)
