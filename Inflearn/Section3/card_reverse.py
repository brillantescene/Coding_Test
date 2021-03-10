import sys
sys.stdin = open('Inflearn/in5.txt', 'r')

# card = [i for i in range(0, 21)]
card = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    # m = s + (e-s+1)//2
    # for j in range(s, m):
    #     tmp = card[j]
    #     card[j] = card[e]
    #     card[e] = tmp
    #     e -= 1
    for i in range((e-s+1)//2):
        card[s+i], card[e-i] = card[e-i], card[s+i]
print(*card[1:])
