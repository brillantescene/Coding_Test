def hanoiTower(num, f, by, to):
    if num == 1:
        print(f"원반1: {f}에서 {to}로 이동")
    else:
        hanoiTower(num-1, f, to, by)
        print(f"원반{num}: {f}에서 {to}로 이동")
        hanoiTower(num-1, by, f, to)


hanoiTower(4, "A", "B", "C")
