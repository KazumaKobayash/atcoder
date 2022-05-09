N, A, B = map(int, input().split())

for i in range(N):
    for k in range(A):
        for l in range(N):
            for j in range(B):
                if (i+l) % 2 == 0:
                    print(".", end="")
                else:
                    print("#", end="")
        print()