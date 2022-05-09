'''
https://atcoder.jp/contests/abc116/tasks/abc116_c
茶色の人の半数が 80分で解ける問題（https://chokudai.hatenablog.com/entry/2019/02/11/155904）
'''


def main():
    N = int(input())
    H = list(map(int, input().split())) 
    cnt = 0
    while sum(H) != 0:
        f = False
        for i in range(N):
            if H[i] != 0:
                H[i] -= 1
                f = True
            elif f:
                cnt += 1
                break
            if f and i == N-1:
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    main()