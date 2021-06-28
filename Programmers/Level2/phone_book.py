# 해시
# 전화번호 목록

# 근데 해시 풀이가 아님,,
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        length = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:length]:
            return False
    return True
