# numpy を使った実装
import numpy as np

MOD =  998244353
N, M, K, S, T, X = map(int, input().split())
T -= 1
S -= 1
X -= 1
U, V = [], []
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    U.append(u)
    V.append(v)
dp = np.zeros((N, K+1, 2), np.int32)

dp[S, 0, 0] = 1

for i in range(K):
    for u, v in zip(U, V):
        for f in range(2):
            dp[u, i+1, f] += dp[v, i, f ^ (X==u)]
            dp[u, i+1, f] %= MOD
            dp[v, i+1, f] += dp[u, i, f ^ (X==v)]
            dp[v, i+1, f] %= MOD   
print(dp[T, K, 0])

# 解説を参考にしつつ自分で書いたコード（ほぼ解説のコードのまま）
# MOD =  998244353
# N, M, K, S, T, X = map(int, input().split())
# T -= 1
# S -= 1
# X -= 1
# U, V = [], []
# for i in range(M):
#     u, v = map(int, input().split())
#     u -= 1
#     v -= 1
#     U.append(u)
#     V.append(v)

# dp = [[[0]*N for _ in range(K+1)] for _ in range(2)]
# dp[0][0][S] = 1
# for i in range(1, K+1):
#     for u, v in zip(U, V):
#         for j in range(2):
#             dp[j][i][u] += dp[j ^ (X == u)][i-1][v]
#             if dp[j][i][u] >= MOD:
#                 dp[j][i][u] -= MOD
#             dp[j][i][v] += dp[j ^ (X == v)][i-1][u]
#             if dp[j][i][v] >= MOD:
#                 dp[j][i][v]-= MOD
# print(dp[0][K][T])


# 解説のコードのコピペ
# MOD = 998244353
# N, M, K, S, T, X = map(int, input().split())
# S -= 1
# T -= 1
# X -= 1

# edge = []
# for i in range(M):
#     U, V = map(int, input().split())
#     U -= 1
#     V -= 1
#     edge.append((U, V))

# dp = [[[0] * N for i in range(K + 1)] for x in range(2)]
# dp[0][0][S] = 1

# for i in range(K):
#     for U, V in edge:
#         for x in range(2):
#             dp[x][i + 1][V] += dp[x ^ (V == X)][i][U]
#             if dp[x][i + 1][V] >= MOD:
#                 dp[x][i + 1][V] -= MOD
#             dp[x][i + 1][U] += dp[x ^ (U == X)][i][V]
#             if dp[x][i + 1][U] >= MOD:
#                 dp[x][i + 1][U] -= MOD

# print(dp[0][K][T])





