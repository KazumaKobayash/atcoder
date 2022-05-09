N = int(input())
l = [i for i in range(1,2*N+2)]
print(l[0])
l.remove(l[0])

while True:
    x = int(input())
    if x == 0:
        break
    l.remove(x)
    print(l[0])
    l.remove(l[0])

    