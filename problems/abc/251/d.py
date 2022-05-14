W = int(input())

n = 150
x = [str(i+1) for i in range(n)]
x = x +[str(3*n-2)]
x = x +[str(3*n-2+(i+1)*2*n) for i in range(300-n-1)]

print(300)
print(" ".join(x))