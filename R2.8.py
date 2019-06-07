for val in range(1,17):
    if wallet[0].charge(val)==False:
        break
    if wallet[0].charge(2*val)==False:
        break
    if wallet[0].charge(3*val)==False:
        break
        
