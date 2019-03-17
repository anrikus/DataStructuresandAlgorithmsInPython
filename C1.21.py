l = []
while True:
    try:
        l.append(input())
    except EOFError:
        break
for x in range(len(l)):
    print(l[-1-x])
        
