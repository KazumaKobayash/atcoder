N = int(input())
A = list(map(int, input().split()))

dp = [-1]*N
dp2 = [-1]*N

dp[0] = A[0]
dp2[0] = A[-1]
print(A)
for i in range(N-2):
    if dp[i] == -1:
        continue
    if i > N-5:
        if A[i+1] < A[i+2]:
            dp[i+1] = dp[i]+ A[i+1]
        else:
            dp[i+1] = dp[i]+ A[i+2]
    else:
        if min(A[i+1]+A[i+3], A[i+1]+A[i+3]) > min(A[i+2]+A[i+3], A[i+2]+A[i+4]):
            dp[i+2] = dp[i]+A[i+2]
        else:
            dp[i+1] = dp[i]+A[i+1]
a1 = [e for e in dp if e != -1][-1]
print(dp)
A = [A[i-1] for i in range(N)]
print(A)
for i in range(N-2):
    if dp2[i] == -1:
        continue
    if i > N-5:
        if A[i+1] < A[i+2]:
            dp2[i+1] = dp2[i]+ A[i+1]
        else:
            dp2[i+1] = dp2[i]+ A[i+2]
    else:
        if min(A[i+1]+A[i+3], A[i+1]+A[i+3]) > min(A[i+2]+A[i+3], A[i+2]+A[i+4]):
            dp2[i+2] = dp2[i]+A[i+2]
        else:
            dp2[i+1] = dp2[i]+A[i+1]
a2 = [e for e in dp2 if e != -1][-1]
print(dp2)
print(min(a1, a2))

# N = int(input())
# A = list(map(int, input().split()))
# A = A

# dp = [-1]*N
# dp2 = [-1]*N
# dp3 = [-1]*N

# dp[0] = A[0]
# dp2[0] = A[1]
# dp3[0] = A[2]

# for i in range(N-3):
#     if dp[i] == -1:
#         continue
#     if min(A[i+1], A[i+2], A[i+3]) == A[i+3]:
#         dp[i+3] = dp[i]+A[i+3]
#     elif min(A[i+1], A[i+2], A[i+3]) == A[i+2]:
#         dp[i+2] = dp[i]+A[i+2]
#     elif min(A[i+1], A[i+2], A[i+3]) == A[i+1]:
#         dp[i+1] = dp[i]+A[i+1]
# a1 = [e for e in dp if e != -1][-1]

# for i in range(N-3):
#     if dp2[i] == -1:
#         continue
#     if min(A[i+1], A[i+2], A[i+3]) == A[i+3]:
#         dp2[i+3] = dp2[i]+A[i+3]
#     elif min(A[i+1], A[i+2], A[i+3]) == A[i+2]:
#         dp2[i+2] = dp2[i]+A[i+2]
#     elif min(A[i+1], A[i+2], A[i+3]) == A[i+1]:
#         dp2[i+1] = dp2[i]+A[i+1]
# a2 = [e for e in dp2 if e != -1][-1]

# for i in range(N-3):
#     if dp3[i] == -1:
#         continue
#     if min(A[i+1], A[i+2], A[i+3]) == A[i+3]:
#         dp3[i+3] = dp3[i]+A[i+3]
#     elif min(A[i+1], A[i+2], A[i+3]) == A[i+2]:
#         dp3[i+2] = dp3[i]+A[i+2]
#     elif min(A[i+1], A[i+2], A[i+3]) == A[i+1]:
#         dp3[i+1] = dp3[i]+A[i+1]
# a3 = [e for e in dp3 if e != -1][-1]

# print(dp)
# print(dp2)
# print(dp3)
# print(min(a1, a2, a3))



