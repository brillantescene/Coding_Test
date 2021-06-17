from collections import deque


def solution(skill, skill_trees):
    cnt = 0

    for skill_tree in skill_trees:
        dq = deque(skill_tree)
        i = 0
        while dq:
            tmp = dq[0]
            if i > len(skill):
                cnt += 1
                break
            if tmp in skill:
                print(tmp, skill[i])
                if skill[i] == tmp:
                    i += 1
                    dq.popleft()
                else:
                    break
            else:
                dq.popleft()
        if not dq:
            cnt += 1
    return cnt


# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CED"]))
print(solution("CBD", ["CED"]))
