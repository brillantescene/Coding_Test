import sys
# for i in range(1, 6):
#     sys.stdin = open(f'Inflearn/in{i}.txt', 'r')


sys.stdin = open('Inflearn/in1.txt', 'r')

a = input()
num = ''
for x in a:
    if x.isdigit():
        num += x
num = int(num)
cnt = 2
for i in range(2, num):
    if num % i == 0:
        cnt += 1
print(num)
print(cnt)
