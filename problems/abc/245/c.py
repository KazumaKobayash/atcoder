N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N
ep = [0] * N

dp[0] = True
ep[0] = True

for i in range(N-1):
    if dp[i]:
        if abs(A[i] - A[i+1]) <= K:
            dp[i+1] = True
        if abs(A[i] - B[i+1]) <= K:
            ep[i+1] = True
    if ep[i]:
        if abs(B[i] - A[i+1]) <= K:
            dp[i+1] = True
        if abs(B[i] - B[i+1]) <= K:
            ep[i+1] = True
if dp[N-1] or ep[N-1]:
    print("Yes")
else:
    print("No")