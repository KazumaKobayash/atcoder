N = int(input())
S, T, A = [], [], []
for i in range(N):
    s, t = input().strip().split()
    S.append(s)
    T.append(t)
f = True
for i in range(N):
    SA = [ele for ele in S]
    SA.pop(i)
    TA = [ele for ele in T]
    TA.pop(i)
    if (S[i] in SA or S[i] in TA) and (T[i] in SA or T[i] in TA):
        f = False

if f:
    print("Yes")
else:
    print("No")