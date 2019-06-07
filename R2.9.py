def __sub__(self, other):
    if len(other)!=len(self):
        raise ValueError("Dimensions must Agree")

    result = Vector(len(self))

    for i in len(self):
        result[j]=self[j]-other[j]

    return(result)
