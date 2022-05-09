

def main():
    N = int(input())
    XY = [0] * N
    for i in range(N):
        XY[i] = list(map(int, input().split()))
    S = input()
    mins = dict()
    maxs = dict()
    flag = False

    for i in range(N):
        
        if S[i] == "R":
            if XY[i][1] in mins:
                mins[XY[i][1]] = min(mins[XY[i][1]], XY[i][0])
            else:
                mins[XY[i][1]] = XY[i][0]
            if XY[i][1] in maxs and maxs[XY[i][1]] > mins[XY[i][1]]:
                flag = True
            
        else:
            if XY[i][1] in maxs:
                maxs[XY[i][1]] = max(maxs[XY[i][1]], XY[i][0])
            else:
                maxs[XY[i][1]] = XY[i][0]
            if XY[i][1] in mins and maxs[XY[i][1]] > mins[XY[i][1]]:
                flag = True

    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()


''' TLE
def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    S = input()
    flag = False

    for i in range(N):
        for j in range(i+1, N):
            if Y[i] == Y[j]:
                if X[i] > X[j] and S[i] == "L" and S[j] == "R":
                    flag = True
                elif X[i] < X[j] and S[i] == "R" and S[j] == "L":
                    flag = True
    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
'''
    