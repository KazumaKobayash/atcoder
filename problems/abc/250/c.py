
def original(N, Q, X):
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

def zero_index(N, Q, X):
    val = [i for i in range(N+1)]
    pos = [i for i in range(N+1)]

    for x in X:
        # print("pos:", pos)
        # print("val:", val)

        p1 = pos[x]
        if pos[x] == N:
            p2 = pos[x] -1
        else:
            p2 = pos[x] +1
        v1 = val[p1]
        v2 = val[p2]

        pos[v1], pos[v2] = pos[v2], pos[v1]
        val[p1], val[p2] = val[p2], val[p1]
    # print("pos:", pos)
    # print("val:", val)
    print(" ".join([str(e) for e in val[1:]]))

def one_index(N, Q, X):
    val = [i+1 for i in range(N)]
    pos = [i for i in range(N)]
    for x in X:
        # print("pos:", pos)
        # print("val:", val)

        p1 = pos[x-1]
        if pos[x-1] == N-1:
            p2 = pos[x-1] -1
        else:
            p2 = pos[x-1] +1
        v1 = val[p1]
        v2 = val[p2]

        pos[v1-1], pos[v2-1] = pos[v2-1], pos[v1-1]
        val[p1], val[p2] = val[p2], val[p1]
    # print("pos:", pos)
    # print("val:", val)
    print(" ".join([str(e) for e in val]))

if __name__ == "__main__":
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    original(N, Q, X)
    zero_index(N, Q, X)
    one_index(N, Q, X)
