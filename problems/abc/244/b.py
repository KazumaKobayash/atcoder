N = int(input())
S = input()

r = [[1,0], [0,-1], [-1,0], [0,1]]
x = 0
ans = [0,0]
for c in S:
    if c =="S":
        ans[0] += r[x][0]
        ans[1] += r[x][1]
    if c =="R":
        x = (x+1) % 4
print(ans[0],ans[1])

