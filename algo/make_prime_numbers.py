def make_pn_list(n):
    pn = [i for i in range(n)]
    for i in range(2, n):
        for j in range(i*2,n,i):
            pn[j] = 0
    pn[0], pn[1] = 0, 0
    return [e for e in pn if e]