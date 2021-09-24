def solution(s):
    answer = ''
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    stack = []
    for ss in s:
        if ss.isalpha():
            stack.append(ss)
        else:
            answer += ss
        if stack:
            num = ''.join(stack)
            if num in dic:
                answer += dic[num]
                stack.clear()
    return answer


print(solution("one4seveneight"))
