
import numpy as np
NUM = 998244353



def main():
    N = int(input())
    dp = np.zeros((N,11))
    for i in range(1,10):
        dp[0][i] = 1
    for n in range(1, N):
        for i in range(1,10):
            dp[n][i] = (dp[n-1][i-1] + dp[n-1][i] + dp[n-1][i+1]) % NUM
    print(int(np.sum(dp[N-1])%NUM))

if __name__ == "__main__":
    main()

# def main():
#     N = int(input())
#     cnt = 0
#     x = [2,3,3,3,3,3,3,3,2]
#     y = [2,3,3,3,3,3,3,3,2]
#     for _ in range(N-2):
#         y[0] = (x[0] + x[1])%NUM
#         y[1] = (x[0] + x[1] + x[2])%NUM
#         y[2] = (x[1] + x[2] + x[3])%NUM
#         y[3] = (x[2] + x[3] + x[4])%NUM
#         y[4] = (x[3] + x[4] + x[5])%NUM
#         y[5] = (x[4] + x[5] + x[6])%NUM
#         y[6] = (x[5] + x[6] + x[7])%NUM
#         y[7] = (x[6] + x[7] + x[8])%NUM
#         y[8] = (x[7] + x[8])%NUM
#         x = [ele for ele in y]
#     print(sum(y)%NUM)
