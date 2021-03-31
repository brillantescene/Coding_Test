import sys
sys.stdin = open('Inflearn/in1.txt', 'r')

n = int(input())
p = {input(): 1 for _ in range(n)}

for _ in range(n-1):
    p[input()] = 0

for key, val in p.items():
    if val:
        print(key)
        break

'''
for _ in range(n-1):
    word.remove(input())
print(word[0])
'''
