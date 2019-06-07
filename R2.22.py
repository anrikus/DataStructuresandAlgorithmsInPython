def __eq__(self, other):
    if len(self)!=len(other):
        return False
    
    for x,y in self, other:
        if x != y:
            return(False)

    return(True)
