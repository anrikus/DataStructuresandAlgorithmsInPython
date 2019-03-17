def norm(v, p=2):
    norm  = 0
    for x in v:
        norm = norm + x**p
    norm  = norm**(1/p)
    return norm
