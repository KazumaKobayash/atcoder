N = int(input())
S = input()
l_l = []
r_l = []
for i in range(N):
    if S[i] == "L":
        r_l.append(str(i))
    if S[i] == "R":
        l_l.append(str(i))
print(" ".join(l_l+[str(N)]+r_l[::-1]))