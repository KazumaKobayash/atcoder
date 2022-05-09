N = int(input())

ans = ["1"]
for i in range(N-1):
    ans = ans+[str(i+2)]+ans
print(" ".join(ans))
