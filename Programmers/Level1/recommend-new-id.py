# 2021 KAKAO BLIND RECRUITMENT
# 신규 아이디 추천

import re


def solution(new_id):
    # 1, 2 단계
    new_id = re.sub('[^a-z0-9-_.]', '', new_id.lower())
    # 3단계
    new_id = re.sub('[.]+', '.', new_id)
    # 4단계
    new_id = re.sub('^[.]|[.]$', '', new_id)
    # 5, 6
    new_id = 'a' if not new_id else new_id[:15]
    new_id = re.sub('^[.]|[.]$', '', new_id)

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id
