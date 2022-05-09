H, W = map(int, input().split())
R, C = map(int, input().split())

cnt = 0
if H - R >= 1:
    cnt += 1
if R > 1:
    cnt += 1
if W - C >= 1:
    cnt += 1
if C > 1:
    cnt += 1
print(cnt)