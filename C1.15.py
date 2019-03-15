def uniq(data):
    for x in data:
        count = 0
        for y in data:
            if x==y:
                count+=1
            if count==2:
                return False
    return True
