inputstr = input()

dict = []
length = len(inputstr)
for i in range(length):
    dict.append(inputstr[i:])
dict.sort()
for str in dict:
    print(str)