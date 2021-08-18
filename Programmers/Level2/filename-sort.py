# 2018 카카오 블라인드 3차
# 파일명 정렬
import re


def solution(files):
    answer = [re.split(r"([0-9]+)", file) for file in files]
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(ans) for ans in answer]


'''
정규식 x
def solution(files):
    answer = []
    for i in range(len(files)):
        ch = 0
        tmp = []
        for j in range(len(files[i])):
            if j != 0 and (not files[i][j].isdigit()) and files[i][j-1].isdigit():
                tmp.append(int(files[i][ch:j]))
                tmp.append(files[i][j:])
                break

            if files[i][j].isdigit() and not files[i][j-1].isdigit():
                tmp.append(files[i][:j])
                ch = j
        answer.append(tmp)
    answer.sort(key=lambda x: (x[0].lower(), x[1]))
    return answer
'''

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress",
                "A-10 Thunderbolt II", "F-14 Tomcat"]))

print(solution(["img12.png", "img10.png", "img02.png",
                "img1.png", "IMG01.GIF", "img2.JPG"]))
