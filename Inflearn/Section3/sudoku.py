import sys
sys.stdin = open('Inflearn/in5.txt', 'r')
'''
s = [list(map(int, input().split())) for _ in range(9)]

res1 = res2 = True
for i in range(9):
    c1 = [0]*10
    c2 = [0]*10
    for j in range(9):
        c1[s[i][j]] = 1
        c2[s[j][i]] = 1
    if sum(c1) != 9 or sum(c1) != 9:
        res1 = False
        break

for i in range(3):
    for j in range(3):
        c3 = [0]*10
        for k in range(3):
            for l in range(3):
                c3[s[k+(i*3)][l+(j*3)]] = 1
        if sum(c3) != 9:
            res2 = False
            break

if res1 and res2:
    print("YES")
else:
    print("NO")
'''


def check(s):
    for i in range(9):
        c1 = [0]*10
        c2 = [0]*10
        for j in range(9):
            c1[s[i][j]] = 1
            c2[s[j][i]] = 1
        if sum(c1) != 9 or sum(c1) != 9:
            return False

    for i in range(3):
        for j in range(3):
            c3 = [0]*10
            for k in range(3):
                for l in range(3):
                    c3[s[k+(i*3)][l+(j*3)]] = 1
            if sum(c3) != 9:
                return False
    return True


s = [list(map(int, input().split())) for _ in range(9)]

if check(s):
    print("YES")
else:
    print("NO")
