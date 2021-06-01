# Summer/Winter Coding(~2018) 예산

def solution(d, budget):
    d.sorted()
    while budget < sum(d):
        d.pop()
    return len(d)
