sentence = input()
count = int(len(sentence) / 10) + 1
for i in range(count):
    print(sentence[i*10:(i+1)*10])