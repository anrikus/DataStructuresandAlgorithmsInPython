def __neg__(self):
    result = Vector(len(self))

    for i in len(self):
        result[j]=-self[j]

    return(result)
