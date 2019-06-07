class Vector:

    def __init__(self, d):

        if isinstance(d, int):

            self._coords = [0]*d

        if isinstance(d, (list, tuple, str)):

            self._coords = []
            for x in range(len(d)):
                self._coords.append(int(x))
                
                
            
