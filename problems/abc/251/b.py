N, W = map(int, input().split())
A = list(map(int, input().split()))
W += 1 
ans = [0]*W
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            x =A[i]+A[j]+A[k]
            if x < W:
                ans[x] = 1
        x = A[i]+A[j]
        if x < W:
            ans[x] = 1
    x = A[i]
    if x < W:
        ans[x] = 1
print(sum(ans))


# s = set()
# for i in range(N):
#     for j in range(i+1, N):
#         for k in range(j+1, N):
#             s.add(A[i]+A[j]+A[k])
#         s.add(A[i]+A[j])
#     s.add(A[i])
# print(sum([1 for e in s if e<=W]))