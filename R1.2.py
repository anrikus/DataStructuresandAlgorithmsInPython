def is_even(k):
    x = str(k)
    if x[-1]=="0" or x[-1]=="2" or x[-1]=="4" or x[-1]=="6" or x[-1]=="8":
        return True
    else:
        return False
