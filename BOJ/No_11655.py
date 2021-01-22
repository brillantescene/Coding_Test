inputstr = list(input())

def ROT13(str):
    cap = [al for al in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    small = [al for al in "abcdefghijklmnopqrstuvwxyz"]
    idx = 0
    result = []
    for ch in str:
        if ch.isupper():
            idx = cap.index(ch) + 13
            if idx > 25:
                idx -= 26
            result.append(cap[idx])
        elif ch.islower():
            idx = small.index(ch) + 13
            if idx > 25:
                idx -= 26
            result.append(small[idx])
        else:
            result.append(ch)

    return result

if __name__ == "__main__":
    for ch in ROT13(inputstr):
        print(ch, end='')