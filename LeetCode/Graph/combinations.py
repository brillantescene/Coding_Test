class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(level, start):
            if level == k:
                result.append(res[:])
                return
            for i in range(start, n+1):
                res[level] = i
                dfs(level+1, i+1)

        res = [0] * k
        result = []
        dfs(0, 1)

        return result


'''
다른 방법
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(elements, start, k):
            if k == 0:
                result.append(elements[:])
                return
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()
        
        dfs([], 1, k)
        
        return result
'''
'''
itertools 사용
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations(range(1, n+1), k)
'''
