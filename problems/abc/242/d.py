
def main():
    S = input()
    S_len = len(S)
    Q = int(input())
    T, K = [], []
    for _ in range(len(Q)):
        t, k = map(int,input().split())
        T.append(t)
        K.append(k)
    
    for i in range(len(Q)):
        a = 1
        while True:
            if K[i] <= a * S_len:
                break
            a *= 2
        cnt = 1
        for j in range(S_len):
            if a * (j+1) <= K[i]:
                cnt += 1
        b = K[i] - a*cnt
        while True:
            c = b // 2
        start_word = S[cnt]



            


if __name__ == "__main__":
    main()