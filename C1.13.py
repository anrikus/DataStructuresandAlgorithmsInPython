def reverse(data):
    if len(data)%2==0:
        for x in range(int(len(data)/2)):
            data[x], data[-1-x] = data[-1-x], data[x]
    else:
        for x in range(int(len(data)-1)/2):
            data[x], data[-1-x] = data[-1-x], data[x]
    return data
