'''
https://atcoder.jp/contests/abc116/tasks/abc113_c
緑の人の半数が 60分で解ける問題（https://chokudai.hatenablog.com/entry/2019/02/11/155904）
'''

# # tel になった解答
# def main():
#     N, M = map(int, input().split())
#     PY = [list(map(int, input().split())) for _ in range(M)]

#     sPY = sorted(PY, key=lambda x:x[1])
#     for P,Y in PY:
#         cnt = 1
#         for i in range(M):
#             if sPY[i][1]==Y:
#                 print(f"{str(P).zfill(6)}{str(cnt).zfill(6)}")
#             if sPY[i][0]==P:
#                 cnt +=1


# # tel になった解答
# def main():
#     N, M = map(int, input().split())
#     PY = [list(map(int, input().split())) for _ in range(M)]

#     KP = [[] for _ in range(N)]
#     for P, Y in PY:
#         KP[P-1].append(Y)
#     for i in range(N):
#         KP[i].sort()
#     for P,Y in PY:
#         x = KP[P-1].index(Y) + 1
#         print(f"{str(P).zfill(6)}{str(x).zfill(6)}")

def main():
    N, M = map(int, input().split())
    PYc = [list(map(int, input().split()))+[e_i] for e_i, _ in enumerate(range(M))]
    KP = [[] for _ in range(N)]
    for P, Y, c in PYc:
        KP[P-1].append((Y, c))
    for i in range(N):
        KP = sorted(KP[i], key=lambda x:x[0])
    
    ans = []
    for i in range(N):
        for e_j, y, c in enumerate(KP[i]):
            ans.append((e_j+1, i+1, c))
    ans = sorted(ans, key=lambda x:x[2])
    for b, p, c in ans:
        print(f"{str(p).zfill(6)}{str(b).zfill(6)}")


        

    
    for P,Y in PY:
        x = KP[P-1].index(Y) + 1
        print(f"{str(P).zfill(6)}{str(x).zfill(6)}")

if __name__ == "__main__":
    main()