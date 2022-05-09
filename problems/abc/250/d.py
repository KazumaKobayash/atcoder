# from time import time
# s = time()
N = int(input())
n = 1_000_000
pn = {i+1: 1 for i in range(n)}
pn[1] = 0
pn[n] = 0
for i in range(2, n):
    if pn[i]:
        for j in range(i*2, n, i):
            pn[j] = 0
pn = [k for k,v in pn.items() if v]
pn2 = [e*e*e for e in pn]
cnt = 0
l = len(pn)
for i in range(l-1):
    for j in range(i+1, l):
        x = pn[i] * pn2[j]
        if x > 1e18:
            break
        if x < N+1:
            cnt += 1
print(cnt)
# print(time() -s)