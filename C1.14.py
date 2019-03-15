def if_odd(seq):
    odd_count = 0
    for x in seq:
        if x%2!=0:
            odd_count+=1
        if odd_count==2:
            return True
    return False
