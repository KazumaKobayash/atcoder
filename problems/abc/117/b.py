'''
https://atcoder.jp/contests/abc117/tasks/abc117_b
茶色の人の半数が５分で解ける問題（https://chokudai.hatenablog.com/entry/2019/02/11/155904）
'''
def main():
    N = int(input())
    L = list(map(int, input().split()))
    if sum(L) > 2*max(L):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
