'''
https://atcoder.jp/contests/abc235/tasks/abc235_d
key word:幅優先探索
'''

from collections import deque

def main():
    a, N = map(int, input().split())
    lim = 1
    while lim < N:
        lim *= 10
    q = deque()
    q.append(1)
    cnt = [-1] * lim
    cnt[1] = 0
    while q:
        val = q.popleft()
        nv1 = val * a

        if (nv1 < lim) and (cnt[nv1] == -1):
            cnt[nv1] = cnt[val] + 1
            q.append(nv1)
        if (val >= 10) and (val % 10 != 0):
            nv2 = int(str(val)[-1] + str(val)[:-1])
            if cnt[nv2] == -1:
                cnt[nv2] = cnt[val] + 1
                q.append(nv2)
    print(cnt[N])

if __name__ == "__main__":
    main()