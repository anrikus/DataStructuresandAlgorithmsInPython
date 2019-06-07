def recursive_hanoi(n, origin, temp, target):

    if n==1:
        
        print("Move {0} from {1} to {3}".format(n, origin, temp, target))

    else:

        recursive_hanoi(n-1, origin, target, temp)

        print("Move {0} from {1} to {3}".format(n, origin, temp, target))

        recursive_hanoi(n-1, temp, origin, target)
