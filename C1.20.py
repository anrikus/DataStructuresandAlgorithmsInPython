import random

def rand_order(data):
    for x in range(len(data)):
        r = random.randint(0, len(data) - 1)
        data[x], data[r] = data[r], data[x]
