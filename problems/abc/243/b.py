
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        if A[i] == B[i]:
            cnt1 += 1
            A[i] = -1

    for i in range(N):
        if B[i] in A:
            cnt2 += 1
    
    print(cnt1)
    print(cnt2)
        
if __name__ == "__main__":
    main()