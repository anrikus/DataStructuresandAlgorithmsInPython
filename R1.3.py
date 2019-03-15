def minmax(data):
    smallest = data[0]
    largest = data[0]
    for x in data:
        if x < smallest:
            smallest = x
        if x > largest:
            largest = x
    return smallest, largest
