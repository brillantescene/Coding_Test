def solution(n, words):
    answer = []
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
            return [(i % n)+1, (i//n)+1]
    else:
        return [0, 0]


'''
def solution(n, words):
    answer = []
    prev = ''
    p = [0] * n
    stack = []
    idx = 0
    for word in words:
        idx += 1
        if not prev:
            prev = word
            stack.append(word)
        else:
            if prev[-1] == word[0] and word not in stack:
                print(word)
                stack.append(word)
                prev = word
            else:
                answer = [idx, p[idx-1]+1]
                break

        p[idx-1] += 1
        if len(stack) % n == 0:
            idx = 0
    else:
        answer = [0, 0]
    return answer
'''

print(solution(3, ["tank", "kick", "know", "wheel",
                   "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage",
                   "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, 	["hello", "one", "even", "never", "now", "world", "draw"]))
