def check(time):
    cnt = 0
    while time >= 0:
        for x in times:
            time -= x
            if time >= 0:
                cnt += 1
    print(cnt)
    print()
    return cnt


n = 6
times = [7, 10]
answer = 0

l = 1
r = n*max(times)

while l <= r:
    mid = (l+r)//2
    print(mid)
    if check(mid) <= n:

        r = mid - 1
    else:
        answer = mid
        l = mid + 1
print(answer)
