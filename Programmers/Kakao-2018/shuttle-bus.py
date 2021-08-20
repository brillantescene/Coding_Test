# level 3
# 셔틀 버스
def solution(n, t, m, timetable):
    con = 0
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()
    current = 540
    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0] <= current:
                con = timetable.pop(0) - 1
            else:
                con = current
        current += t
    h, m = divmod(con, 60)
    return str(h).zfill(2)+':'+str(m).zfill(2)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
