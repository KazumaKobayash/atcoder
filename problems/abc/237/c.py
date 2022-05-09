S = input()
f = True
cntB = len(S) - len(S.rstrip("a"))
cntF = len(S) - len(S.lstrip("a"))
if cntB-cntF > 0:
    S = "a"* (cntB-cntF) + S
if S == S[::-1]:
    print("Yes")
else:
    print("No")

''' ↓ac するが冗長なコード
S = input()
f = True
cntB = 0
cntF = 0
 
for i in range(len(S)):
    if S[-(i+1)] == "a":
        cntB += 1
    else:
        break
 
for i in range(len(S)):
    if S[i] == "a":
        cntF += 1
    else:
        break
 
if cntB < cntF:
    f = False
else:
    if not (cntB-cntF==0):
        S = S[:-(cntB-cntF)]
for i in range(len(S)):
    if not S[i]==S[len(S)-1-i]:
        f = False
 
if f:
    print("Yes")
else:
    print("No")
'''