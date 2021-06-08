
# 내가 제출한 답
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        for x in s:
            if x.isalnum():
                if x.isupper():
                    tmp.append(x.lower())
                else:
                    tmp.append(x)
        return tmp == tmp[::-1]

# 정규식을 사용하면?


class Solution_2:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
