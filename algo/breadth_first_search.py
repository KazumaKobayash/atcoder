'''幅優先探索
https://atcoder.jp/contests/atc002/tasks/abc007_3
リストだと、xとyが逆になる。

'''

from collections import deque
from pprint import pprint
INF = 10**6

def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1
    mp = [list(input()) for _ in range(R)]
    dist = [[INF for _ in range(C)] for _ in range(R)]
    
    q = deque()
    q.append([sx, sy])
    dist[sy][sx] = 0
    move = [[0,1], [1,0], [0,-1], [-1,0]] 
    while q:
        now = q.popleft()
        d = dist[now[1]][now[0]]
        for i in range(4):
            nxt = [now[0]+move[i][0], now[1]+move[i][1]]
            if nxt[0]<0 or nxt[0]>C:
                continue
            if nxt[1]<0 or nxt[1]>R:
                continue
            if mp[nxt[1]][nxt[0]] == '#':
                continue
            if dist[nxt[1]][nxt[0]] != INF:
                continue

            dist[nxt[1]][nxt[0]] = d + 1
            q.append(nxt)
    return dist[gy][gx]

if __name__ == "__main__":
    print(main())