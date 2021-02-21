arr = [5, 3, 7, 9, 2, 5, 2, 6]
min = float('inf')  # 무한대 값
# min = arr[0]
for i in arr:
    if i < min:
        min = i
print(min)
