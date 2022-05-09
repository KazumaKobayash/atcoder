N, Q = map(int, input().split())
X = [int(input()) for _ in range(Q)]
l = [i+1 for i in range(N)]
d = {i+1:i for i in range(N)}
for x in X:
    if d[x]+1 == N:
        l[d[x]], l[d[x]-1] = l[d[x]-1], l[d[x]]
        d[l[d[x]]], d[l[d[x]-1]] = d[l[d[x]-1]], d[l[d[x]]]
    else:
        l[d[x]], l[d[x]+1] = l[d[x]+1], l[d[x]]
        d[l[d[x]]], d[l[d[x]+1]] = d[l[d[x]+1]], d[l[d[x]]]
print(" ".join([str(e) for e in l]))
