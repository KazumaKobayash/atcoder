
N = int(input())
S = []
for i in range(N):
    S.append(input())
flag = False
for i in range(N):
    for j in range(N):
        if j > 4:
            cnt_y = 0
            for k in range(6):
                if S[i][j-k] == "#":
                    cnt_y += 1
            if cnt_y >= 4:
                flag = True
        if i > 4:
            cnt_t = 0
            for k in range(6):
                if S[i-k][j] == "#":
                    cnt_t += 1
            if cnt_t >= 4:
                flag = True
        if j < N-5 and i < N-5:
            cnt_n1 = 0
            for k in range(6):
                if S[i+k][j+k] == "#":
                    cnt_n1 += 1
            if cnt_n1 >= 4:
                flag = True
        if j > 4 and i < N-5:
            cnt_n2 = 0
            for k in range(6):
                if S[i+k][j-k] == "#":
                    cnt_n2 += 1
            if cnt_n2 >= 4:
                flag = True

if flag:
    print("Yes")
else:
    print("No")
        

            

        