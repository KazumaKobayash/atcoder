from collections import deque
d = deque()
Q = int(input())
st =0
rest = None
Qs = []
for _ in range(Q):
    Qs.append(list(map(int, input().split())))
for q in Qs:
    if q[0] == 2:
        x = 0
        l = q[1]
        while True:
            y = None
            if rest:
                y = rest
            else:
                y = d.popleft()
            if y[1] < l:
                x += y[1]*y[0]
                l -= y[1]
                rest = None
            else:
                x += y[0]*l
                rest = (y[0],y[1]-l)
                break
        print(x)
    if q[0] == 1:
        d.append((q[1], q[2]))

