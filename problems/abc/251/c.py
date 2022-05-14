N = int(input())
ST = [[ele[0], int(ele[1])] for ele in [list(input().split()) for _ in range(N)]]
S = set()

max_v = -1
ans = -1
for i, st in enumerate(ST):
    if st[0] in S:
        continue
    S.add(st[0])
    if st[1] > max_v:
        ans = i+1
        max_v = st[1]
print(ans)

