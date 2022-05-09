
def main():
    N, X = map(int,input().split())
    S = input()
    root = []

    while True:
        if X > 1 :
            if X % 2 == 1:
                root.append("R")
                X = X // 2
            elif X % 2 == 0:
                root.append("L")
                X = X // 2
        else:
            break
    root = root[::-1]

    for i in range(N):
        if S[i] == "U":
            root.pop()
        if S[i] == "L":
            root.append("L")
        if S[i] == "R":
            root.append("R")
    
    ans = 1
    for i in range(len(root)):
        if root[i] == "L":
            ans *= 2
        if root[i] == "R":
            ans = ans*2 + 1
    print(ans)

if __name__ == "__main__":
    main()